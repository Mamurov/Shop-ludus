# Generated by Django 3.2.7 on 2021-10-05 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_purchases_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Purchases',
            new_name='Order',
        ),
    ]
