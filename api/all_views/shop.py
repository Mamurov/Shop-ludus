from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import decorator_from_middleware


from ..services.token import TokenService
from ..models import User, Order
from ..all_serializers.order import OrderSerializer
from ..all_serializers.user import ShopUserSerializer
from ..all_middlewares.shop import isShopCheckMiddleware


def outLimit(limit):
    if isinstance(limit, type("")):
        return int(limit);
    return None;

class OutShopProductView(APIView):
    @decorator_from_middleware(isShopCheckMiddleware)
    def get(self, request):
        shopId = request.data.get('shopId', 0);
        offset = request.query_params.get('offset', 0);
        limit = request.query_params.get('limit', None);
        data = Order.objects.distinct().filter(cart__children__productId__shop=shopId).order_by('-id')[int(offset):outLimit(limit)];
        serializer = OrderSerializer(data, many=True);
        return Response(serializer.data);

class CheckIsShopOwnerView(APIView):
    def get(self, request):
        authMeta = request.META["authorization"];
        accessToken = authMeta.split(" ")[1];
        userData = TokenService.validateAccessToken(accessToken);
        user = User.objects.get(id=userData["id"]);
        data = ShopUserSerializer(user).data;
        if data["isShopOwner"] and data["shop"]:
            return Response(data={'result': True});
        return Response(data={'result': False}, status=status.HTTP_400_BAD_REQUEST);