# Generated by Django 3.2.7 on 2021-10-04 14:14

import api.all_models.catalog
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_purchases_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='catalog',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=api.all_models.catalog.rename, verbose_name='Иконка'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('cartId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cart')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
    ]
