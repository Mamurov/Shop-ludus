# Generated by Django 3.2.7 on 2021-10-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_purchases_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]
