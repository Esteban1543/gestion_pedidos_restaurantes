from typing import Self

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from gpr_api.common.utilities.pagination_response import paginate_data
from gpr_api.users.filters.user import UserFilter
from gpr_api.users.selectors.get_user import get_users
from gpr_api.users.serializers.login import LoginSerializer
from gpr_api.users.serializers.users import UserAdditionalDataSerializer, UserSerializer
from gpr_api.users.serializers.users_massive import UserMassiveUploadSerializer
from gpr_api.users.utilities.get_authenticated_user import get_authenticated_user


class LoginAPIView(APIView):
    def post(self: Self, request: Request) -> Response:
        user = LoginSerializer()
        token = user.validate(request.data)

        return Response(data={"access_token": token}, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    def get(self: Self, request: Request) -> Response:
        get_authenticated_user(request=request)
        queryset: QuerySet = get_users()
        user_filter: QuerySet = UserFilter(request.query_params, queryset=queryset).qs
        user_serializer: dict = UserSerializer(user_filter, many=True).data
        return paginate_data(data=user_serializer, request=request)

    def post(self: Self, request: Request) -> Response:
        get_authenticated_user(request=request)
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        return Response(data=user_serializer.data, status=status.HTTP_201_CREATED)


class ChangePasswordAPIView(APIView):
    def patch(self: Self, request: Request, user_id: int) -> Response:
        get_authenticated_user(request=request)
        user_additional_data_serializer = UserAdditionalDataSerializer(
            data={**request.data, "user_id": user_id}
        )
        user_additional_data_serializer.is_valid(raise_exception=True)

        return Response(
            data={"message": "Password changed successfully"}, status=status.HTTP_200_OK
        )


class MassiveUserUploadAPIView(APIView):
    def post(self: Self, request: Request) -> Response:
        get_authenticated_user(request=request)
        massive_user_upload_serializer = UserMassiveUploadSerializer(data=request.data)
        massive_user_upload_serializer.is_valid(raise_exception=True)

        return Response(data={"detail": "Users were created correctly"}, status=status.HTTP_200_OK)
