from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from ..models import Cart, CartItem, Product
from ..all_serializers.cart import CartSerializer, CartItemSerializer, NotDetailCartSerializer
from django.utils.decorators import decorator_from_middleware
from ..all_middlewares.cart import CartMiddleware


class CartView(APIView):
    @decorator_from_middleware(CartMiddleware)
    def get(self, request):
        cartId = request.COOKIES.get('cartId', "");
        cart = get_object_or_404(Cart, cartId=cartId);
        serializer = CartSerializer(cart, context={'request': request});
        return Response(serializer.data);
    @decorator_from_middleware(CartMiddleware)
    def delete(self, request):
        cartId = request.COOKIES.get('cartId', "");
        CartItem.objects.filter(cartId=cartId).delete();
        return Response();

class CartCheckView(APIView):
    @decorator_from_middleware(CartMiddleware)
    def post(self, request):
        cartId = request.COOKIES.get('cartId', "");
        try:
            cart = Cart.objects.get(cartId=cartId);
            serializer = NotDetailCartSerializer(cart, context={'request': request}).data;
            response = Response();
            response.set_cookie(
                'cartId',
                serializer["cartId"],
                httponly=True,
                max_age=60 * 60 * 24 * 30
            )
            return response;
        except:
            newCart = NotDetailCartSerializer(data={}, partial=True);
            newCart.is_valid(raise_exception=True);
            newCart.save();
            response = Response();
            response.set_cookie(
                'cartId',
                newCart.data["cartId"],
                httponly=True,
                max_age=60 * 60 * 24 * 30
            )
            return response;

class SingleCartItemView(APIView):
    @decorator_from_middleware(CartMiddleware)
    def put(self, request):
        productId = request.data.get('productId', 0);
        count = request.data.get('count', 0);
        if not productId and not count:
            return Response(status=status.HTTP_400_BAD_REQUEST);
        cartId = request.COOKIES.get('cartId', "");
        cart = NotDetailCartSerializer(Cart.objects.get(cartId=cartId)).data;
        get_object_or_404(Product, id=productId);
        try:
            cartItem = CartItem.objects.get(cartId=cart["id"], productId=productId);
            changedCartItem = CartItemSerializer(cartItem, data={'count': count}, partial=True);
            changedCartItem.is_valid(raise_exception=True);
            changedCartItem.save();
        except:
            serializer = CartItemSerializer(data={'cartId': cart["id"], 'count': count, 'productId': productId}, partial=True);
            serializer.is_valid(raise_exception=True);
            serializer.save();
        return Response(status=status.HTTP_200_OK);
    @decorator_from_middleware(CartMiddleware)
    def delete(self, request):
        cartId = request.COOKIES.get('cartId', "");
        productId = request.data.get('productId', 0);
        try:
            cart = Cart.objects.get(cartId=cartId);
            serializer = NotDetailCartSerializer(cart, context={'request': request}).data;
            cartItem = CartItem.objects.get(cartId=serializer["id"], productId=productId);
            cartItem.delete();
            return Response();
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST);