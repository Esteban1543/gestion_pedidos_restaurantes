from django.urls import path

from .views.reports import ReportView

urlpatterns = [
    path("reports/<int:restaurants_id>", ReportView.as_view(), name="reports"),
]
