from datetime import datetime, timedelta, timezone
from typing import Any, Self

import jwt
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginAPIView(APIView):
    def post(self: Self, request: Request) -> Response:
        user: str = getattr(request, "user", "")
        # password: str = getattr(request, "password", "")

        payload: dict[str, Any] = {
            "user": user,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=5),
            "iat": datetime.now(timezone.utc),
        }

        token: str = jwt.encode(payload, "asd123", algorithm="HS256")

        return Response(data={"token": token}, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    def get(self: Self, request: Request) -> Response:
        return Response(status=status.HTTP_200_OK)
