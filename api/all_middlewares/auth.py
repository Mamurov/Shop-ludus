from rest_framework.response import Response
from rest_framework import status
from ..services.token import TokenService
from ..constants.notAuthMessage import notAuthMsg

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request);
        return response;
    def process_view(self, request, view_func, view_args, view_kwargs):
        authMeta = request.request.headers.get("authorization", "0 0");
        if not authMeta:
            return Response(notAuthMsg, status=status.HTTP_401_UNAUTHORIZED);
        accessToken = authMeta.split(" ")[1];
        if not accessToken:
            return Response(notAuthMsg, status=status.HTTP_401_UNAUTHORIZED);
        userData = TokenService.validateAccessToken(accessToken);
        if not userData:
            return Response(notAuthMsg, status=status.HTTP_401_UNAUTHORIZED);
        return view_func(request, *view_args, **view_kwargs);
