# Generated by Django 3.0.7 on 2020-06-18 13:37

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_order_billing_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='countries',
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(default='india', max_length=2),
            preserve_default=False,
        ),
    ]
