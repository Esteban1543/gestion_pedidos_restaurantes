"""
URL configuration for gpr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Crear el esquema de la API
schema_view = get_schema_view(
    openapi.Info(
        title="Gpr API",
        default_version="v1",
        description="Sistema gestion de pedidos restaurantes",
        contact=openapi.Contact(email="jhoanestebanpv1@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include("gpr_api.users.urls")),
    path("", include("gpr_api.menus.urls")),
    path("", include("gpr_api.restaurants.urls")),
    path("", include("gpr_api.orders.urls")),
    path("", include("gpr_api.reports.urls")),
]
