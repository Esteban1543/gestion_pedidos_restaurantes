from typing import Self

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from gpr_api.orders.serializers.creaate_orders import CreateOrderSerializer


class CreateOrderView(APIView):
    def post(self: Self, request: Request) -> Response:
        order_serializer = CreateOrderSerializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()
        return Response(
            data={"message": "Su orden se cargo correctamente", "data": order_serializer.data},
            status=status.HTTP_200_OK,
        )
