from ariadne_jwt.decorators import login_required
from .models import Customer


@login_required
def all_customers(*_):
    customers = Customer.objects.all()
    return customers

@login_required
def get_customer(*_, customerId):
    customer = Customer.objects.get(pk=customerId)
    return {"success": True, "customer": customer, "errors": None}


@login_required
def create_customer(_, info, name):
    customer = Customer.objects.create(name=name)
    return {"success": True, "customer": customer, "errors": None}

@login_required
def edit_customer(_, info, customerId, name):
    customer = Customer.objects.get(pk=customerId)
    customer.name = name
    customer.save()
    return {"success": True, "customer": customer, "errors": None}

@login_required
def delete_customer(*_, customerId):
    Customer.objects.get(pk=customerId).delete()
    return {"success": True, "errors": None}
