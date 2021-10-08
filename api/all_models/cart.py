from django.db import models
import uuid

class Cart(models.Model):
    cartId = models.UUIDField(verbose_name="Id корзины", null=True, blank=True);
    def __str__(self):
        return self.cartId.__str__();
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.cartId = uuid.uuid4()
        super(Cart, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
