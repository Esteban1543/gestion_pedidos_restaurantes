from django.db.models import QuerySet

from gpr_api.menus.models.menus import Menus


def get_menus() -> QuerySet[Menus]:
    return Menus.objects.all()
