from rest_framework import serializers
from ..models import SubCatalog
from .category import CategorySerializer


class SubCatalogSerializer(serializers.ModelSerializer):
    children = CategorySerializer(many=True);
    class Meta:
        model = SubCatalog
        fields = "__all__"