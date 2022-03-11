from django.db import models
from django_countries.fields import CountryField


class Salutation(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Customer(models.Model):

    customer_number = models.PositiveIntegerField()
    salutation = models.ForeignKey(
        "Salutation", on_delete=models.PROTECT, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    phone = models.CharField(max_length=100, blank=True, default="")
    mobile = models.CharField(max_length=100, blank=True, default="")
    email = models.CharField(max_length=100, blank=True, default="")
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
