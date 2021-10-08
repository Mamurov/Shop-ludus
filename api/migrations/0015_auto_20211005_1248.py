# Generated by Django 3.2.7 on 2021-10-05 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20211005_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='orderId',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.cart', verbose_name='Корзина'),
            preserve_default=False,
        ),
    ]