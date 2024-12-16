from django.db.models import QuerySet

from gpr_api.restaurants.models.restaurants import Restaurants


def get_restaurants() -> QuerySet[Restaurants]:
    return Restaurants.objects.all()


def get_restaurant_by_id(*, restaurant_id: int) -> QuerySet[Restaurants]:
    return Restaurants.objects.filter(id=restaurant_id)
