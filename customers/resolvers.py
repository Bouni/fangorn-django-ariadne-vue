from .models import Customer


def all_customers(*_):
    customers = Customer.objects.all()
    return customers 

def get_customer(*_, customerId):
    customer = Customer.objects.get(pk=customerId)
    return {'success': True, 'customer': customer, 'errors': None}

def create_customer(_,info, version, title):
    customer = Customer.objects.create(version=version, title=title)      
    return {'success': True, 'customer': customer, 'errors': None}


