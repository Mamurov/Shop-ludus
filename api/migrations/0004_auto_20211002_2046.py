# Generated by Django 3.2.7 on 2021-10-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211002_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='title_slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка для seo'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка для seo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(db_index=True, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_count',
            field=models.IntegerField(db_index=True, default=0, verbose_name='Цифра продажи'),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='surname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='subcatalog',
            name='title_slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка для seo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
