import datetime
from typing import Self

import jwt
from rest_framework import serializers

from gpr_api.users.models.users import Users
from gpr_api.users.serializers.users import UserSerializer


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self: Self, attrs: dict) -> str:
        email = attrs.get("email")
        password = attrs.get("password")

        user: Users | None = Users.objects.filter(
            email=email, usersadditionaldata__password=password
        ).first()
        if not user:
            raise serializers.ValidationError({"detail": "Invalid credentials"})

        user_serializer: UserSerializer = UserSerializer(user)

        return self._create_token(user_serializer.data)

    def _create_token(self: Self, user_data: dict) -> str:
        payload: dict = {
            "user": user_data,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1),
        }

        token: str = jwt.encode(payload, "asd123", algorithm="HS256")

        return token
