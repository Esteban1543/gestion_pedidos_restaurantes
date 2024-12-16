from django.db.models import QuerySet

from gpr_api.users.models.users import Users


def get_users() -> QuerySet[Users]:
    return Users.objects.all()


def get_user_by_id(*, user_id: int) -> QuerySet[Users]:
    return Users.objects.filter(id=user_id)
