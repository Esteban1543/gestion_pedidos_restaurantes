import django_filters

from gpr_api.restaurants.models.restaurants import Restaurants


class RestaurantsFilter(django_filters.FilterSet):
    category_id = django_filters.NumberFilter(field_name="category__id")

    class Meta:
        model = Restaurants
        fields = [
            "id",
            "name",
            "address",
            "rating",
            "status",
            "category",
            "latitude",
            "longitude",
        ]
