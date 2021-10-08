from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..services.token import TokenService
from ..all_serializers.user import UserCRUDSerializer, ProfileSerializer
from ..models import User
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
from ..utils.profileSerialize import profileSerialize

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', "");
        password = request.data.get('password', "");
        user = get_object_or_404(User, email=email);
        data = UserCRUDSerializer(user).data;
        match = bcrypt.checkpw(password.encode('utf8'), data["password"].encode('utf8'));
        if not match:
            return Response(data={'message': 'Неправильный пароль'}, status=status.HTTP_400_BAD_REQUEST);
        tokens = TokenService.generateTokens({'id': data["id"]});
        tokenIsSaved = TokenService.saveToken(data, tokens["refreshToken"]);
        if not tokenIsSaved:
            return Response(status=status.HTTP_401_UNAUTHORIZED);
        response = Response(data={
            'profile': profileSerialize(user, request),
            'accessToken': tokens["accessToken"],
        }, status=status.HTTP_200_OK);
        response.set_cookie(
            'refreshToken',
            tokens["refreshToken"],
            httponly=True,
            max_age=60 * 60 * 24 * 30
        );
        return response;

class RegisterView(APIView):
    def post(self, request):
        data = request.data;
        email = request.data.get("email", "");
        try:
            user = User.objects.get(email=email);
            return Response(data={'message': 'Пользователь с таким email '+ email +' уже существует'}, status=status.HTTP_400_BAD_REQUEST);
        except ObjectDoesNotExist:
            user = None;
        result = UserCRUDSerializer(data=data, context={'request': request});            
        result.is_valid(raise_exception=True);
        result.save();
        tokens = TokenService.generateTokens({'id': result.data["id"]});
        tokenIsSaved = TokenService.saveToken(result.data, tokens["refreshToken"]);
        if not tokenIsSaved:
            return Response(status=status.HTTP_401_UNAUTHORIZED);
        response = Response(data={'profile': profileSerialize(result.instance, request), 'accessToken': tokens["accessToken"]},status=status.HTTP_200_OK);
        response.set_cookie(
            'refreshToken',
            tokens["refreshToken"],
            httponly=True,
            max_age=60 * 60 * 24 * 30
        );
        return response;

class RefreshView(APIView):
    def get(self, request):
        refreshToken = request.COOKIES.get("refreshToken", "");
        result = TokenService.refresh(refreshToken, request);
        if result["isAuth"] == True:
            response = Response(data={
                "profile": result["profile"],
                "accessToken": result["tokens"]["accessToken"] 
            });
            response.set_cookie(
                'refreshToken',
                result["tokens"]["refreshToken"],
                httponly=True,
                max_age=60 * 60 * 24 * 30
            );
            return response;
        else: 
            return Response(status=status.HTTP_401_UNAUTHORIZED);