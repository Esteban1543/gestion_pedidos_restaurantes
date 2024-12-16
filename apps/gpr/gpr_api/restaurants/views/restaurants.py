from typing import Self

from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from gpr_api.common.utilities.pagination_response import paginate_data
from gpr_api.restaurants.filters.restaurants import RestaurantsFilter
from gpr_api.restaurants.models.restaurants import Restaurants
from gpr_api.restaurants.selectors.restaurants import get_restaurants
from gpr_api.restaurants.serilizers.restaurants import RestaurantsSerializer
from gpr_api.users.utilities.get_authenticated_user import get_authenticated_user


class RestaurantsListAPIView(APIView):
    def get(self: Self, request: Request) -> Response:
        get_authenticated_user(request=request)
        restaurants_queryset: QuerySet = get_restaurants()
        restaurants_filters: QuerySet[Restaurants] = RestaurantsFilter(
            request.query_params, queryset=restaurants_queryset
        ).qs
        restaurants_serializer: RestaurantsSerializer = RestaurantsSerializer(
            restaurants_filters, many=True
        )

        return paginate_data(request=request, data=restaurants_serializer.data)
