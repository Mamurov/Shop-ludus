from rest_framework import serializers
from ..models import Catalog
from .subcatalog import SubCatalogSerializer

class CatalogSerializer(serializers.ModelSerializer):
    children = SubCatalogSerializer(many=True);
    class Meta:
        model = Catalog
        fields = "__all__"