from typing import Self

from rest_framework import serializers

from gpr_api.menus.models.menus import Menus
from gpr_api.menus.selectors.get_menus import get_menus
from gpr_api.restaurants.models.restaurants import Restaurants
from gpr_api.restaurants.selectors.restaurants import get_restaurant_by_id


class MenuCategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()


class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    preparation_time = serializers.IntegerField(required=False)
    available = serializers.BooleanField(required=False)
    image_url = serializers.URLField(required=False)
    restaurants_id = serializers.IntegerField(required=False)

    def validate(self: Self, attrs: dict) -> dict:
        restaurant_id: int = attrs.get("restaurants_id", None)
        menu_id: int = attrs.get("id", None)

        if not restaurant_id:
            raise serializers.ValidationError({"detail": "Restaurant ID is required"})

        self._validate_restaurant(restaurant_id=restaurant_id)

        if not menu_id:
            self._create_menu(attrs=attrs)

            return attrs

        menu: Menus = self._validate_menu(menu_id=menu_id)

        self._update_menu(menu=menu, attrs=attrs)

        return attrs

    def _validate_menu(self: Self, *, menu_id: int) -> Menus:
        menu: Menus | None = get_menus().first()

        if not menu:
            raise serializers.ValidationError({"detail": "Menu does not exist"})

        return menu

    def _validate_restaurant(self: Self, *, restaurant_id: int) -> None:
        restaurant: Restaurants | None = get_restaurant_by_id(restaurant_id=restaurant_id).first()

        if not restaurant:
            raise serializers.ValidationError({"detail": "Restaurant does not exist"})

    def _create_menu(self: Self, *, attrs: dict) -> None:
        Menus.objects.create(**attrs)

    def _update_menu(self: Self, *, menu: Menus, attrs: dict) -> None:
        for key, value in attrs.items():
            setattr(menu, key, value)

        menu.save()
