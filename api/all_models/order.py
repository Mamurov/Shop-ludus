from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя", null=True, blank=True);
    surname = models.CharField(max_length=200, verbose_name="Фамилия", null=True, blank=True);
    email = models.EmailField(verbose_name="Email", null=True, blank=True);
    inn = models.IntegerField(verbose_name="ИИН");
    phone = models.CharField(max_length=100, verbose_name="Телефон", null=True, blank=True);
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, verbose_name="Корзина");
    user = models.ForeignKey("User", verbose_name="Пользователь", null=True, blank=True, on_delete=models.CASCADE, db_index=True, related_name="orders");
    def __str__(self): 
        return self.email;