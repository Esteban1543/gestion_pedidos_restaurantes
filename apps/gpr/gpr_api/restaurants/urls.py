from django.urls import path

from .views.restaurants import RestaurantsListAPIView

urlpatterns = [
    path("restaurants", RestaurantsListAPIView.as_view(), name="restaurants"),
]
