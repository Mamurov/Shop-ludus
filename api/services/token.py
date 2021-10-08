import jwt
import datetime
from django.conf import settings

from api.all_models.user import User
from api.all_serializers.user import UserCRUDSerializer, ProfileSerializer
from ..all_serializers.token import TokenSerializer
from ..models import Token
from django.core.exceptions import ObjectDoesNotExist



class TokenService():
    def generateTokens(payload):
        accessToken = jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 30), **payload}, settings.JWT_ACCESS_TOKEN, algorithm="HS256");
        refreshToken = jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 60 * 24 * 30), **payload}, settings.JWT_REFRESH_TOKEN, algorithm="HS256");
        
        return{
            'accessToken': accessToken.decode('utf8'),
            'refreshToken': refreshToken.decode('utf8')
        }
    def validateAccessToken(token):
        try:
            decoded = jwt.decode(token, settings.JWT_ACCESS_TOKEN, algorithms=["HS256"]);
            return decoded;
        except:
            return False;
    def validateRefreshToken(token):
        try:
            decoded = jwt.decode(token, settings.JWT_REFRESH_TOKEN, algorithms=["HS256"]);
            return decoded;
        except:
            return False;
    def saveToken(user, refreshToken):
        try:
            token = Token.objects.get(userId=user["id"]);
            serializer = TokenSerializer(token, data={'refreshToken': refreshToken}, partial=True);
            if serializer.is_valid():
                serializer.save();
                return True;
            else:
                return False;
        except ObjectDoesNotExist:
            serializer = TokenSerializer(data={'userId': user["id"], 'refreshToken': refreshToken});
            if serializer.is_valid():
                serializer.save();
                return True;
            else:
                return serializer.errors;
    def removeToken(refreshToken):
        try:
            tokenFromDb = Token.objects.get(refreshToken=refreshToken);
            tokenFromDb.delete();
            return tokenFromDb;
        except:
            return None;
    def findToken(refreshToken):
        try:
            tokenFromDb = Token.objects.get(refreshToken=refreshToken);
            return tokenFromDb;
        except:
            return None;

    def refresh(refreshToken, request):
        if not refreshToken:
            return {
                'isAuth': False
            }
        try:
            userData = TokenService.validateRefreshToken(refreshToken);
            tokenFromDb = TokenService.findToken(refreshToken);
            if not userData or not tokenFromDb:
                return {
                    'isAuth': False
                }
            user = User.objects.get(id=userData["id"]);
            if not user:
                return {
                    'isAuth': False
                }
            serializer = UserCRUDSerializer(user).data;
            tokens = TokenService.generateTokens({'id': serializer["id"]});
            tokenSavedResult = TokenService.saveToken(serializer, tokens["refreshToken"]);
            if not tokenSavedResult:
                return {
                    'isAuth': False
                }
            return {
                'isAuth': True,
                'tokens': tokens,
                'profile': ProfileSerializer(user, context={'request': request}).data
            }
        except:
            return {
                'isAuth': False
            }
