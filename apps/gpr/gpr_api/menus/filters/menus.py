import django_filters

from gpr_api.menus.models.menus import Menus


class MenuFilter(django_filters.FilterSet):
    restaurants_id = django_filters.NumberFilter(field_name="restaurants__id")

    class Meta:
        model = Menus
        fields = [
            "id",
            "name",
            "description",
            "price",
            "preparation_time",
            "available",
            "restaurants",
        ]
