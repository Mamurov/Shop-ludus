from ..all_serializers.user import ProfileSerializer


def profileSerialize(instance, request):
    profile = ProfileSerializer(instance, context={'request': request});
    return profile.data;