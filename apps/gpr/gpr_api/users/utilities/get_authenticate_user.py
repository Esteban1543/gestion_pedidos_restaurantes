from httpx import Request


def get_authenticate_user(request: Request) -> dict[str, str]:
    user = getattr(request, "user")
    password = getattr(request, "password")

    payload = {
        "user": user,
        "exp": datetime.utcnow() + timedelta(minutes=5),
        "iat": datetime.utcnow(),
    }

    token = jwt.encode(payload, "asd123", algorithm="HS256")

    return {"token": token}
