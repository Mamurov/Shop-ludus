from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..models import Order
from ..all_serializers.order import OrderSerializer
from django.utils.decorators import decorator_from_middleware
from ..all_middlewares.auth import AuthMiddleware
from ..services.token import TokenService


class OrderView(APIView):
    @decorator_from_middleware(AuthMiddleware)
    def get(self, request):
        authMeta = request.headers.get("authorization");
        accessToken = authMeta.split(" ")[1];
        userData = TokenService.validateAccessToken(accessToken);
        data = Order.objects.filter(user=userData["id"]);
        serializer = OrderSerializer(data).data;
        return Response(serializer);
    def post(self, request):
        orderBody = request.data.get('order', "");
        serializer = OrderSerializer(data=orderBody, partial=True);
        serializer.is_valid(raise_exception=True);
        serializer.save();
        return Response("");
    