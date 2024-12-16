from typing import Self

from django.db import transaction
from rest_framework import serializers

from gpr_api.restaurants.models.restaurants import Restaurants
from gpr_api.restaurants.selectors.restaurants import get_category_by_id, get_restaurant_by_id


class RestaurantsCategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()


class RestaurantsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255, required=True)
    address = serializers.CharField(required=True)
    rating = serializers.FloatField(required=True)
    status = serializers.CharField(max_length=20, required=True)
    active = serializers.BooleanField(required=True)
    category_id = serializers.IntegerField()
    latitude = serializers.DecimalField(max_digits=21, decimal_places=11, required=True)
    longitude = serializers.DecimalField(max_digits=21, decimal_places=11, required=True)

    @transaction.atomic
    def validate(self: Self, attrs: dict) -> dict:
        restaurant_id: int = attrs.get("id", None)
        category_id: int = attrs.get("category_id", None)

        self._validate_category_id(category_id=category_id)

        if restaurant_id:
            restaurant: Restaurants = self._validate_restaurant_id(restaurant_id=restaurant_id)
            self._update_restaurant(restaurant=restaurant, attrs=attrs)
            return attrs

        self._create_restaurant(attrs=attrs)

        return attrs

    def _validate_category_id(self: Self, *, category_id: int) -> None:
        category = get_category_by_id(category_id=category_id).first()

        if not category:
            raise serializers.ValidationError({"detail": "Category not found"})

    def _validate_restaurant_id(self: Self, *, restaurant_id: int) -> Restaurants:
        restaurant = get_restaurant_by_id(restaurant_id=restaurant_id).first()

        if not restaurant:
            raise serializers.ValidationError({"detail": "Restaurant not found"})

        return restaurant

    def _create_restaurant(self: Self, *, attrs: dict) -> None:
        Restaurants.objects.create(**attrs)

    def _update_restaurant(self: Self, *, restaurant: Restaurants, attrs: dict) -> None:
        for key, value in attrs.items():
            setattr(restaurant, key, value)

        restaurant.save()
