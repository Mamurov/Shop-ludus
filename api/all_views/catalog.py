from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..all_serializers.catalog import CatalogSerializer
from ..models import Catalog


class CatalogView(APIView):
    def get(self, request):
        catalogs = Catalog.objects.all();
        data = CatalogSerializer(catalogs, many=True, context={'request': request});
        return Response(data=data.data);