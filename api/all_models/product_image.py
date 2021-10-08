from django.db import models
import os
import uuid
from .product import Product


def rename(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('images/products/', filename)

class ProductImage(models.Model):
    productId = models.ForeignKey("Product", on_delete=models.PROTECT, verbose_name="Товар", related_name="images", db_index=True);
    image = models.ImageField(upload_to=rename);

    def __str__(self):
        return self.productId.title;