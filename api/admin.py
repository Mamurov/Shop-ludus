from re import S
from django.contrib import admin
from .models import *
from .admin_settings.user import UserAdmin
from .admin_settings.cart import CartAdmin
from .admin_settings.shop import ShopAdmin
from .admin_settings.product import ProductAdmin
from .admin_settings.order import OrderAdmin

# Register your models here.

admin.site.register(Product, ProductAdmin);
admin.site.register(Catalog);
admin.site.register(SubCatalog);
admin.site.register(ProductImage);
admin.site.register(User, UserAdmin);
admin.site.register(Token);
admin.site.register(Shop, ShopAdmin);
admin.site.register(Category);
admin.site.register(Order, OrderAdmin);
admin.site.register(Cart, CartAdmin);
admin.site.register(CartItem);