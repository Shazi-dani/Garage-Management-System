from django.urls import path

from .views import DashboardView
from .views import (
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    AppointmentDetailView,
    AppointmentCreateAPIView,
    AppointmentUpdateAPIView,
    AppointmentDeleteAPIView,
    AppointmentListView,
    AppointmentAllView,
)

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('create_appointment/', AppointmentCreateView.as_view(), name='create_appointment'),
    path('edit_appointment/<int:pk>/', AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('delete_appointment/<int:pk>/', AppointmentDeleteView.as_view(), name='delete_appointment'),
    path('appointment_detail/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('api/appointments/', AppointmentListView.as_view(), name='appointments'),
    path('api/appointments_all/', AppointmentAllView.as_view(), name='appointments_all'),
    path('api/create_appointment/', AppointmentCreateAPIView.as_view(), name='api_create_appointment'),
    path('api/edit_appointment/<int:pk>/', AppointmentUpdateAPIView.as_view(), name='api_edit_appointment'),
    path('api/delete_appointment/<int:pk>/', AppointmentDeleteAPIView.as_view(), name='api_delete_appointment'),
]
