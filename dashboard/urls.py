from django.urls import path

from .views import HomeView, DashboardView
from .views import AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView, test_view
from .views import submit_inquiry, vehicle_list, submit_interest
from django.conf.urls import handler404, handler403, handler500
from dashboard import views

handler404 = 'dashboard.views.custom_404'
handler403 = 'dashboard.views.custom_403'
handler500 = 'dashboard.views.custom_500'

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
     path('test/', test_view, name='test_view'),
]


