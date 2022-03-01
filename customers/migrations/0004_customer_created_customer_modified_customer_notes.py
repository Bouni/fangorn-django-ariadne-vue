# Generated by Django 4.0.2 on 2022-03-01 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0003_salutation_remove_customer_type_customer_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
