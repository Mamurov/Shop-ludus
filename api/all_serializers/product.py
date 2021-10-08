from django.db import models
from rest_framework import fields, serializers
from rest_framework import serializers
from ..models import Product, ProductImage, Shop



class ProductShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop;
        fields = "__all__";


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage;
        exclude = ("productId", );

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True);
    shop = ProductShopSerializer();
    class Meta:
        model = Product;
        fields = "__all__";
