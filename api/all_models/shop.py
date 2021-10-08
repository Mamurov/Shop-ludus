from django.db import models
import uuid
import os

def rename(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('images/shops/', filename)

class Shop(models.Model):
    title = models.CharField(max_length=100, verbose_name="Имя", db_index=True);
    image = models.ImageField(upload_to=rename);

    def __str__(self):
        return self.title;