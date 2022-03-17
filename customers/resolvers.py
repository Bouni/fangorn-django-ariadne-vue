from ariadne import QueryType, MutationType
from ariadne_jwt.decorators import login_required
from django_countries import countries
from .models import Customer, Salutation

query = QueryType()
mutation = MutationType()

@query.field("allCountries")
@login_required
def all_countries(*_):
    return countries

@query.field("allSalutations")
@login_required
def all_salutations(*_):
    salutations = Salutation.objects.all()
    return salutations

@query.field("allCustomers")
@login_required
def all_customers(*_):
    customers = Customer.objects.all()
    return customers


@query.field("customer")
@login_required
def get_customer(*_, customerId):
    try:
        customer = Customer.objects.get(pk=customerId)
        return {"success": True, "customer": customer, "errors": None}
    except Exception as error:
        return {"success": False, "customer": None, "errors": [str(error)]}


@mutation.field("createCustomer")
@login_required
def create_customer(_, info, input):
    input.pop("id")
    input.pop("customer_number")
    input["salutation"] = Salutation.objects.filter(name=input["salutation"]["name"]).first()
    input["country"] = input["country"]["code"] 
    customer = Customer.objects.create(**input)
    return {"success": True, "customer": customer, "errors": None}


@mutation.field("editCustomer")
@login_required
def edit_customer(_, info, customerId, input):
    customer = Customer.objects.get(pk=customerId)
    customer.update(input)
    return {"success": True, "customer": customer, "errors": None}


@mutation.field("deleteCustomer")
@login_required
def delete_customer(*_, customerId):
    Customer.objects.get(pk=customerId).delete()
    return {"success": True, "errors": None}
