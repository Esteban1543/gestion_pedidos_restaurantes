from django.db.models import QuerySet

from gpr_api.restaurants.models.restaurants import Restaurants, RestaurantsCategories


def get_restaurants() -> QuerySet[Restaurants]:
    return Restaurants.objects.filter(active=True)


def get_restaurant_by_id(*, restaurant_id: int) -> QuerySet[Restaurants]:
    return Restaurants.objects.filter(id=restaurant_id)


def get_category_by_id(*, category_id: int) -> QuerySet[RestaurantsCategories]:
    return RestaurantsCategories.objects.filter(id=category_id)
