from django.db import models


class Category(models.Model):
    title_kg = models.CharField(max_length=200, verbose_name="Имя на кыргызском");
    title_ru = models.CharField(max_length=200, verbose_name="Имя на русском");
    title_slug = models.SlugField(max_length=200, verbose_name="Ссылка для seo", unique=True, db_index=True);
    parent = models.ForeignKey("SubCatalog", on_delete=models.PROTECT, related_name="children", db_index=True);

    def __str__(self):
        return self.title_kg;