import jwt
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request


def get_authenticated_user(*, request: Request) -> None:
    token = request.headers.get("Authorization", "")

    try:
        data = jwt.decode(token, "asd123", algorithms=["HS256"])
        return data.get("user")
    except jwt.ExpiredSignatureError:
        raise ValidationError({"error": "Token has expired"})
    except jwt.InvalidTokenError:
        raise ValidationError({"error": "Invalid token"})
