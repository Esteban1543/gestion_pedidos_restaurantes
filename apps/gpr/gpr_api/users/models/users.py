from django.db import models

from gpr_api.common.models.CommonInfo import CommonInfo
from gpr_api.restaurants.models.restaurants import Restaurants


class UsersTypologyTypes(CommonInfo):
    name = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta(CommonInfo.Meta):
        db_table = "users_typology_types"
        ordering = ["id"]


class Users(CommonInfo):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    default_adress = models.TextField()
    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    typology = models.ForeignKey(UsersTypologyTypes, on_delete=models.CASCADE)

    class Meta(CommonInfo.Meta):
        db_table = "users"
        ordering = ["id"]


class UsersAdditionalData(CommonInfo):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)

    class Meta(CommonInfo.Meta):
        db_table = "users_additional_data"
        ordering = ["id"]
