from django.urls import path

from .views.menus import MenusListAPIView

urlpatterns = [
    path("menus", MenusListAPIView.as_view(), name="menus"),
]
