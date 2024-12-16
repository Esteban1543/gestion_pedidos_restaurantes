from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response


def paginate_data(*, data, request: Request) -> Response:
    page_size: int = request.query_params.get("page_size", 10)
    paginator = PageNumberPagination()
    paginator.page_size = page_size

    result_page = paginator.paginate_queryset(data, request)

    return paginator.get_paginated_response(result_page)
