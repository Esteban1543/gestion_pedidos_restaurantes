import csv
from io import TextIOWrapper
from typing import Self

from django.core.files.uploadedfile import UploadedFile as File
from django.db import transaction
from rest_framework import serializers

from gpr_api.users.models.users import Users


class UserMassiveUploadSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)

    def validate(self: Self, attrs: dict) -> dict:
        file: File | None = attrs.get("file")

        if not file:
            raise serializers.ValidationError({"detail": "File is required"})

        users_massive: list = self._destructure_data(file=file)

        if len(users_massive) > 20:
            raise serializers.ValidationError({"detail": "Maximum of 20 users allowed"})

        self._validate_duplicate_email(users_massive=users_massive)

        self._validate_user(users_massive=users_massive)

        self._create_users(users_massive=users_massive)

        return attrs

    def _destructure_data(self: Self, *, file: File) -> list:
        decoded_file = TextIOWrapper(file, encoding="utf-8")

        csv_reader = csv.DictReader(decoded_file)

        return [row for row in csv_reader]

    def _validate_duplicate_email(self: Self, *, users_massive: list) -> None:
        emails = [user["email"] for user in users_massive]

        if len(emails) != len(set(emails)):
            raise serializers.ValidationError({"detail": "Duplicate emails are not allowed"})

    def _validate_user(self: Self, *, users_massive: list) -> None:
        user_alredy_exists = []
        for user in users_massive:
            user_validate = Users.objects.filter(email=user["email"]).exists()

            if user_validate:
                user_alredy_exists.append(user["email"])

        if user_alredy_exists:
            raise serializers.ValidationError(
                {"detail": f"User already exists, {user_alredy_exists}"}
            )

    @transaction.atomic
    def _create_users(self: Self, *, users_massive: list) -> None:
        for user in users_massive:
            Users.objects.create(**user)
