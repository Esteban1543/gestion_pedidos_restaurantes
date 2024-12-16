from typing import Self

from rest_framework import serializers

from gpr_api.users.models.users import Users
from gpr_api.users.selectors.get_user import get_user_by_id


class UsersTypologyTypesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    descripcion = serializers.CharField()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    email = serializers.CharField(max_length=255, required=False)
    phone = serializers.CharField(max_length=20, required=False)
    active = serializers.BooleanField(required=False)
    default_adress = serializers.CharField(required=False)
    restaurants_id = serializers.IntegerField(required=False)
    typology_id = serializers.IntegerField(required=False)

    def validate(self: Self, attrs: dict) -> dict:
        id: int = attrs.get("id", 0)

        user: Users | None = get_user_by_id(user_id=id).first()

        if not user:
            self._create_user(attrs=attrs)
            return attrs

        self._update_user(user=user, attrs=attrs)
        return attrs

    def _create_user(self: Self, *, attrs: dict) -> None:
        Users.objects.create(**attrs)

    def _update_user(self: Self, *, user: Users, attrs: dict) -> None:
        for key, value in attrs.items():
            setattr(user, key, value)

        user.save()


class UserAdditionalDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    password = serializers.CharField(max_length=255)
