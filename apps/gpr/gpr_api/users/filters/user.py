import django_filters

from gpr_api.users.models.users import Users


class UserFilter(django_filters.FilterSet):
    restaurants_id = django_filters.NumberFilter(field_name="restaurants__id")
    typology_id = django_filters.NumberFilter(field_name="typology__id")

    class Meta:
        model = Users
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "default_adress",
            "restaurants",
            "typology",
        ]
