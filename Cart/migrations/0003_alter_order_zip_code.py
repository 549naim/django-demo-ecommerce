# Generated by Django 4.0.4 on 2022-06-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
