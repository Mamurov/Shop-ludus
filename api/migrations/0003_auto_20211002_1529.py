# Generated by Django 3.2.7 on 2021-10-02 12:29

import api.all_models.catalog
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_purchases'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='icon',
            field=models.ImageField(default='', upload_to=api.all_models.catalog.rename, verbose_name='Иконка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0.0, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchases',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user', verbose_name='Пользователь'),
        ),
    ]
