from rest_framework import serializers
from ..models import Token
from django.core.exceptions import ValidationError

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"
