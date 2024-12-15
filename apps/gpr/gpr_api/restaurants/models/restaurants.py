from django.db import models

from gpr_api.common.models.CommonInfo import CommonInfo


class RestaurantsCategories(CommonInfo):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta(CommonInfo.Meta):
        db_table = "restaurants_categories"


class Restaurants(CommonInfo):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.FloatField()
    status = models.CharField(max_length=20)
    category = models.ForeignKey(RestaurantsCategories, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=21, decimal_places=11)
    latitude = models.DecimalField(max_digits=21, decimal_places=11)

    class Meta(CommonInfo.Meta):
        db_table = "restaurants"
