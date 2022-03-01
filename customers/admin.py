from django.contrib import admin

from customers.models import Customer, Salutation

admin.site.register(Customer)
admin.site.register(Salutation)
# Register your models here.
