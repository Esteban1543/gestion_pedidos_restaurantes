from typing import Self

from rest_framework import serializers

from gpr_api.users.models.users import Users, UsersAdditionalData
from gpr_api.users.selectors.get_additional_data import get_additional_data_by_id
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
    id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=True)
    password = serializers.CharField(max_length=255, required=True)

    def validate(self: Self, attrs: dict) -> dict:
        user_id: int = attrs.get("user_id", 0)

        user_additional_data: UsersAdditionalData | None = get_additional_data_by_id(
            user_id=user_id
        ).first()

        if user_additional_data:
            self._update_password(user_additional_data=user_additional_data, attrs=attrs)

        return attrs

    def _update_password(
        self: Self, *, user_additional_data: UsersAdditionalData, attrs: dict
    ) -> None:
        user_additional_data.password = attrs.get("password", user_additional_data.password)
        user_additional_data.save()
