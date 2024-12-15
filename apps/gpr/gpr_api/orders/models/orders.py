from django.db import models

from gpr_api.common.models.CommonInfo import CommonInfo
from gpr_api.menus.models.menus import Menus
from gpr_api.restaurants.models.restaurants import Restaurants
from gpr_api.users.models.users import Users


class Orders(CommonInfo):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    special_instructions = models.TextField()
    estimated_delivery_time = models.DateTimeField()

    class Meta(CommonInfo.Meta):
        db_table = "orders"


class OrdersItems(CommonInfo):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menus, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

    class Meta(CommonInfo.Meta):
        db_table = "orders_items"
