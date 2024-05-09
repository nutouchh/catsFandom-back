from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = get_user_model()
        fields = "__all__"
