from django.urls import path

from .views import HomeView, DashboardView
from .views import AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView
from .views import submit_inquiry, vehicle_list, submit_interest

app_name = "dashboard"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("vehicles/", vehicle_list, name="vehicle_list"),
    path("submit-inquiry/", submit_inquiry, name="submit_inquiry"),
    path("submit-interest/<int:vehicle_id>/", submit_interest, name="submit_interest"),
    path(
        "appointments/new/", AppointmentCreateView.as_view(), name="create_appointment"
    ),
    path(
        "appointments/<int:pk>/edit/",
        AppointmentUpdateView.as_view(),
        name="edit_appointment",
    ),
    path(
        "appointments/<int:pk>/delete/",
        AppointmentDeleteView.as_view(),
        name="delete_appointment",
    ),
]
