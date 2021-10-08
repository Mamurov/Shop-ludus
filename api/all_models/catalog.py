from django.db import models
import uuid
import os

def rename(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('images/icons/', filename)

class Catalog(models.Model):
    title_kg = models.CharField(max_length=200, verbose_name="Имя на кыргызском");
    title_ru = models.CharField(max_length=200, verbose_name="Имя на русском");
    title_slug = models.SlugField(max_length=200, verbose_name="Ссылка для seo", unique=True, db_index=True);
    icon = models.ImageField(upload_to=rename, verbose_name="Иконка", null=True, blank=True);

    def __str__(self):
        return self.title_kg;
