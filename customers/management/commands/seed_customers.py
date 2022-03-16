from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from customers.models import Customer, Salutation

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, default=1)

    def handle(self, *args, **options):
        fake = Faker('de_DE')
        cn = Customer.objects.order_by('-customer_number').first()
        cn = int(cn.customer_number)
        for i in range(1, int(options['number'])+1):
            s = Salutation.objects.order_by("?").first()
            c = Customer(
                    customer_number=cn+i,
                    salutation = s,
                    name = fake.last_name(),
                    firstname = fake.last_name(),
                    address = fake.street_address(),
                    city = fake.city(),
                    zipcode = fake.postcode(),
                    country = fake.country_code(),
                    phone = fake.phone_number(),
                    mobile = fake.phone_number(),
                    email = fake.email(),
                    notes = fake.paragraph(nb_sentences=2)
                    )
            c.save()
            print(f"Fake customer {c} added")
