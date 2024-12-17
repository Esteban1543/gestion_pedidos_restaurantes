from typing import Self

from django.utils import timezone
from rest_framework import serializers


class ReportFiltersSerializer(serializers.Serializer):
    restaurants_id = serializers.IntegerField(required=True)
    start_date = serializers.DateTimeField(required=False, format="%Y-%m-%dT%H:%M:%S.%fZ")
    end_date = serializers.DateTimeField(required=False, format="%Y-%m-%dT%H:%M:%S.%fZ")

    def validate(self: Self, attrs: dict) -> dict:
        start_date = attrs.get("start_date", None)
        end_date = attrs.get("end_date", None)

        if not start_date:
            attrs["start_date"] = timezone.now() - timezone.timedelta(days=30)

        if not end_date:
            attrs["end_date"] = timezone.now()
        return attrs
