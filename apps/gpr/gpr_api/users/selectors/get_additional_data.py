from django.db.models import QuerySet

from gpr_api.users.models.users import UsersAdditionalData


def get_additional_data_by_id(user_id: int) -> QuerySet[UsersAdditionalData]:
    return UsersAdditionalData.objects.filter(user_id=user_id)
