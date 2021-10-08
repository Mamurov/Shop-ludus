from rest_framework.views import APIView
from rest_framework.response import Response
from ..all_serializers.user import ProfileCRUDSerializer
from ..models import User
from django.shortcuts import get_object_or_404
from ..services.token import TokenService
from django.utils.decorators import decorator_from_middleware
from ..all_middlewares.auth import AuthMiddleware
from ..utils.profileSerialize import profileSerialize


class ProfileView(APIView):
    @decorator_from_middleware(AuthMiddleware)
    def get(self, request):
        authMeta = request.headers.get("authorization", "a a");
        accessToken = authMeta.split(" ")[1];
        userData = TokenService.validateAccessToken(accessToken);
        data = get_object_or_404(User, id=userData["id"]);
        serializer = profileSerialize(data, request);
        return Response(serializer);
    @decorator_from_middleware(AuthMiddleware)
    def put(self, request):
        body = request.data.get('data');
        authMeta = request.headers.get("authorization", "a a");
        accessToken = authMeta.split(" ")[1];
        userData = TokenService.validateAccessToken(accessToken);
        user = get_object_or_404(User, id=userData["id"]);
        serializer = ProfileCRUDSerializer(user, data=body, context={'request': request}, partial=True);
        serializer.is_valid(raise_exception=True);
        serializer.save();
        profile = profileSerialize(serializer.instance, request);
        return Response(profile);