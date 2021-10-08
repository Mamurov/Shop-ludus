from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..constants.shopUrls import shopUrls
from ..services.token import TokenService
from ..models import User
from ..all_serializers.user import UserCRUDSerializer
from ..constants.notAuthMessage import notAuthMsg

class isShopCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        return response;
    def process_view(self, request, view_func, view_args, view_kwargs):
        authMeta = request.request.headers.get("authorization");
        if not authMeta:
            return Response(notAuthMsg, status=status.HTTP_401_UNAUTHORIZED);
        accessToken = authMeta.split(" ")[1];
        if not accessToken:
            return Response(notAuthMsg, status=status.HTTP_401_UNAUTHORIZED);
        userData = TokenService.validateAccessToken(accessToken);
        if not userData:
            return Response(notAuthMsg, status=status.HTTP_401_UNAUTHORIZED);
        user = get_object_or_404(User, id=userData["id"]);
        data = UserCRUDSerializer(user).data;
        if not data["isShopOwner"]:
            return Response(data={'message': 'Вы не являетесь владельцем магазина'}, status=status.HTTP_400_BAD_REQUEST);
        return view_func(request, *view_args, **view_kwargs);