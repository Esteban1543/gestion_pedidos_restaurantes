from django.urls import path

from .views.users import UserAPIView

urlpatterns = [
    path("", UserAPIView.as_view(), name="users"),
]
