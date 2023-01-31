from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "is_superuser", "is_staff", "is_active", "groups", "user_permissions"]

        extra_kwargs = {
            "email": {"read_only": True}
        }
