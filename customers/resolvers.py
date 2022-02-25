from .models import Customer


def all_customers(*_):
    customers = Customer.objects.all()
    return customers


def get_customer(*_, customerId):
    customer = Customer.objects.get(pk=customerId)
    return {"success": True, "customer": customer, "errors": None}


def create_customer(_, info, name):
    customer = Customer.objects.create(name=name)
    return {"success": True, "customer": customer, "errors": None}
