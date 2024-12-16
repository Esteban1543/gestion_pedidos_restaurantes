from django.urls import path

from .views.users import ChangePasswordAPIView, LoginAPIView, UserAPIView

urlpatterns = [
    path("login", LoginAPIView.as_view(), name="login"),
    path("users", UserAPIView.as_view(), name="users"),
    path("change-password/<int:user_id>", ChangePasswordAPIView.as_view(), name="change-password"),
]
