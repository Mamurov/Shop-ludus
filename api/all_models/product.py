from django.db import models

parametersForNull = {
    'null': True,
    'blank': True
}

class Product(models.Model):
    price_kg = models.IntegerField(verbose_name="Цена kg", db_index=True);
    price_ru = models.IntegerField(verbose_name="Цена ru", db_index=True);
    previous_price_kg = models.IntegerField(verbose_name="Старая цена", **parametersForNull);
    previous_price_ru = models.IntegerField(verbose_name="Старая цена", **parametersForNull);
    title = models.CharField(max_length=200, db_index=True, verbose_name="Имя");
    description = models.TextField(verbose_name="Описание", **parametersForNull);
    catalog = models.ForeignKey("Catalog", on_delete=models.PROTECT, verbose_name="Каталог");
    subcatalog = models.ForeignKey("SubCatalog", on_delete=models.PROTECT, verbose_name="Под каталог");
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория");
    sold_count = models.IntegerField(verbose_name="Цифра продажи", default=0, db_index=True);
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE);
    rating = models.FloatField(verbose_name="Рейтинг", db_index=True);
    def __str__(self):
        return self.title;