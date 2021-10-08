import re
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Cart
from ..all_serializers.cart import CartSerializer

class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        return response;
    def process_view(self, request, view_func, view_args, view_kwargs):
        cartId = request.request.COOKIES.get('cartId', "");
        try:
            cart = Cart.objects.get(cartId=cartId);
        except:
            newCart = CartSerializer(data={}, partial=True);
            newCart.is_valid(raise_exception=True);
            newCart.save();
            response = Response(status=status.HTTP_400_BAD_REQUEST);
            response.set_cookie(
                'cartId',
                newCart.data["cartId"],
                httponly=True,
                max_age=60 * 60 * 24 * 30
            );
            return response;
        return view_func(request, *view_args, **view_kwargs);
