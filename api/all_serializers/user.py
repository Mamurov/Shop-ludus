from rest_framework import serializers
from ..models import User
from django.core.exceptions import ValidationError
import bcrypt
from .shop import ShopSerializer


def validate_avatar(image):
    MAX_FILE_SIZE = 12000000
    if image.size > MAX_FILE_SIZE:
        raise ValidationError("File size too big!")

class UserCRUDSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=300);
    name = serializers.CharField(min_length=1, max_length=70);
    surname = serializers.CharField(min_length=1, max_length=100);
    avatar = serializers.ImageField(required=False,validators=[validate_avatar]);
    class Meta:
        model = User;
        fields = "__all__";
    def save(self, **kwargs):
        return super().save(**kwargs);
    def create(self, validated_data):
        user = self.Meta.model.objects.create(**validated_data);
        salt = bcrypt.gensalt(rounds=7);
        hashed = bcrypt.hashpw(user.password.encode('utf8'), salt);
        user.password = hashed.decode("utf-8");
        user.save();
        return user;

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User;
        exclude = ("password",);

class ShopUserSerializer(serializers.ModelSerializer):
    shop = ShopSerializer();
    class Meta:
        model = User;
        exclude = ("password",)

class ProfileCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User;
        fields = "__all__"