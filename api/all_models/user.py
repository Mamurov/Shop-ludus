from django.db import models
from django.contrib.auth.hashers import make_password
import uuid
import os


from rest_framework import validators

def rename(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('images/avatars/', filename)

class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя");
    surname = models.CharField(max_length=200, verbose_name="Фамилия");
    avatar = models.ImageField(upload_to=rename, verbose_name="Изображение", null=True, blank=True);
    email = models.EmailField(verbose_name="Email", unique=True, db_index=True);
    password = models.CharField(max_length=200, verbose_name="Пароль");
    isShopOwner = models.BooleanField(default=False, verbose_name="Имеет магазин?");
    shop = models.ForeignKey("Shop", null=True, blank=True, on_delete=models.DO_NOTHING, db_index=True);

    def __str__(self):
        return self.email;