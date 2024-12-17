from datetime import datetime
from typing import Self

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from gpr_api.reports.selectors.get_report_restaurants import get_report_restaurants_by_id
from gpr_api.reports.serializers.reports import ReportFiltersSerializer
from gpr_api.users.utilities.get_authenticated_user import get_authenticated_user


class ReportView(APIView):
    def get(self: Self, request: Request, restaurants_id: int) -> Response:
        get_authenticated_user(request=request)

        query_params: dict = {
            "restaurants_id": restaurants_id,
            "start_date": datetime.strptime(
                request.query_params.get("start_date", None), "%Y-%m-%dT%H:%M:%SZ"
            ),
            "end_date": datetime.strptime(
                request.query_params.get("end_date", None), "%Y-%m-%dT%H:%M:%SZ"
            ),
        }

        print(query_params)

        reports_serializer: ReportFiltersSerializer = ReportFiltersSerializer(data=query_params)
        reports_serializer.is_valid(raise_exception=True)

        params: list = [value for value in reports_serializer.data.values()]
        reports: list = get_report_restaurants_by_id(params=params)

        return Response(reports)

    # def post(self, request):
    #     file = request.data.get("file")

    #     file_patch = f"uploads/{file.name}"
    #     path = default_storage.save(file_patch, file)

    #     return JsonResponse({"path": path, "message": "File uploaded successfully."})
