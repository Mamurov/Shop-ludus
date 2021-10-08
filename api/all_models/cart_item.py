from django.db import models

class CartItem(models.Model):
    productId = models.ForeignKey("Product", on_delete=models.CASCADE);
    cartId = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="children");
    count = models.IntegerField(verbose_name="Количество");
    def __str__(self):
        return self.count.__str__();