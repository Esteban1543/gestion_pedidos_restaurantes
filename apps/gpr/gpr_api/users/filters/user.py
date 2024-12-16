import django_filters

from gpr_api.users.models.users import Users


class UserFilter(django_filters.FilterSet):
    restaurant_name = django_filters.CharFilter(
        field_name="restaurants__name", lookup_expr="icontains"
    )
    typology_name = django_filters.CharFilter(field_name="typology__name", lookup_expr="icontains")

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
