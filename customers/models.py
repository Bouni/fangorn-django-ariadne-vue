from django.db import models

class CustomerType(models.Model):

    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Customer(models.Model):

    name = models.CharField(max_length=200)
    type = models.ForeignKey("CustomerType", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
