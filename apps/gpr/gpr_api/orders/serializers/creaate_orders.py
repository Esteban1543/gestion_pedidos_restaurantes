from datetime import timedelta
from typing import Self

from django.db import transaction
from django.utils.timezone import now
from rest_framework import serializers

from gpr_api.menus.models.menus import Menus
from gpr_api.orders.models.orders import Orders, OrdersItems


class CreateOrderItemSerializer(serializers.Serializer):
    menu_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    notes = serializers.CharField()


class CreateOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    customer_id = serializers.IntegerField()
    restaurants_id = serializers.IntegerField()
    delivery_address = serializers.CharField()
    special_instructions = serializers.CharField()

    order_items = CreateOrderItemSerializer(many=True)

    @transaction.atomic
    def create(self: Self, validated_data: dict) -> dict:
        data: dict = validated_data.copy()
        restaurant_id: int = data["restaurants_id"]
        order_items: list = data.pop("order_items")

        self._validate_order_items(restaurant_id=restaurant_id, order_items=order_items)

        self._calculate_subtotal_order_items(order_items=order_items)

        self._add_additionl_data_to_order(data=data, order_items=order_items)

        order_id: int = self._create_order(data=data)

        self._add_order_id_to_order_items(order_id=order_id, order_items=order_items)

        self._create_order_items(order_items=order_items)

        return validated_data

    def _validate_order_items(self: Self, *, restaurant_id: int, order_items: list) -> None:
        order_list = [item["menu_item_id"] for item in order_items]

        menu_items = Menus.objects.filter(id__in=order_list, restaurants_id=restaurant_id).count()

        if len(order_list) != menu_items:
            raise serializers.ValidationError({"detail": "Invalid menu items"})

    def _calculate_subtotal_order_items(self: Self, *, order_items: list) -> list:
        for order in order_items:
            price: float | None = (
                Menus.objects.filter(id=order["menu_item_id"])
                .values_list("price", flat=True)
                .first()
            )
            subtotal: float = price * order["quantity"]
            order["sub_total"] = subtotal

        return order_items

    def _calculate_total_order(self: Self, *, order_items: list) -> float:
        total = sum([order["sub_total"] for order in order_items])
        return total

    def _add_additionl_data_to_order(self: Self, data: dict, order_items: list) -> dict:
        data["total_amount"] = self._calculate_total_order(order_items=order_items)
        data["status_id"] = 3  # Completed
        data["estimated_delivery_time"] = now() + timedelta(minutes=45)

        return data

    def _add_order_id_to_order_items(self: Self, order_id: int, order_items: list) -> None:
        for order_item in order_items:
            order_item["order_id"] = order_id

    def _create_order(self: Self, data: dict) -> int:
        order = Orders.objects.create(**data)
        return order.id

    def _create_order_items(self: Self, order_items: list) -> None:
        for order_item in order_items:
            OrdersItems.objects.create(**order_item)
