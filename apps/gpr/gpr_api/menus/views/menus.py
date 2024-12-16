from typing import Self

from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from gpr_api.common.utilities.pagination_response import paginate_data
from gpr_api.menus.filters.menus import MenuFilter
from gpr_api.menus.selectors.get_menus import get_menus
from gpr_api.menus.serializers.menus import MenuSerializer


class MenusListAPIView(APIView):
    def get(self: Self, request: Request) -> Response:
        menus: QuerySet = get_menus()
        menus_filter: QuerySet = MenuFilter(request.query_params, queryset=menus).qs
        menu_serializer: dict = MenuSerializer(menus_filter, many=True).data
        return paginate_data(data=menu_serializer, request=request)