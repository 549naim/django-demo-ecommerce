# Generated by Django 4.0.4 on 2022-05-25 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_availability_product_availability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Availability',
            new_name='availability',
        ),
    ]
