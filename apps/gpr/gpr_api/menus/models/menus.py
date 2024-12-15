from django.db import models

from gpr_api.common.models.CommonInfo import CommonInfo
from gpr_api.restaurants.models.restaurants import Restaurants


class MenusCategories(CommonInfo):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta(CommonInfo.Meta):
        db_table = "menus_categories"


class Menus(CommonInfo):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField()
    available = models.BooleanField()
    image_url = models.URLField()
    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

    class Meta(CommonInfo.Meta):
        db_table = "menus"
