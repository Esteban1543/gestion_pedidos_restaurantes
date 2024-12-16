from django.urls import path

from .views.orders import CreateOrderView

urlpatterns = [
    path("create_order", CreateOrderView.as_view(), name="create_orders"),
]
