from django.db.models import QuerySet

from gpr_api.users.models.users import UsersTypologyTypes


def get_typology() -> QuerySet[UsersTypologyTypes]:
    return UsersTypologyTypes.objects.all()


def get_typology_by_id(*, typology_id: int) -> QuerySet[UsersTypologyTypes]:
    return UsersTypologyTypes.objects.filter(id=typology_id)
