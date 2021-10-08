from rest_framework import serializers
from ..models import Cart, CartItem
from .product import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

class CartItemDetailSerializer(serializers.ModelSerializer):
    productId = ProductSerializer();
    class Meta:
        model = CartItem
        exclude = ("cartId", )

class CartSerializer(serializers.ModelSerializer):
    children = CartItemDetailSerializer(many=True);
    class Meta:
        model = Cart
        fields = "__all__"
class NotDetailCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"