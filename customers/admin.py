from django.contrib import admin

from customers.models import Customer, CustomerType

admin.site.register(Customer)
admin.site.register(CustomerType)
# Register your models here.
