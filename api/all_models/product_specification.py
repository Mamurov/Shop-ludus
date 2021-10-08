from django.db import models


class ProductSpecification(models.Model):
    key = models.CharField(max_length=200, verbose_name="Ключ");
    value = models.CharField(max_length=200, verbose_name="Значение");
    productId = models.ForeignKey("Product", on_delete=models.PROTECT, verbose_name="Товар", related_name="specification", db_index=True);
    def __str__(self):
        return self.key;