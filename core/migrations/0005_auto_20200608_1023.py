# Generated by Django 3.0.6 on 2020-06-08 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_deiscount_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='deiscount_price',
            new_name='discount_price',
        ),
    ]
