from django.urls import path

from .views import DashboardView
from .views import AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView, AppointmentListView, AppointmentAllView


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('appointments/new/', AppointmentCreateView.as_view(), name='create_appointment'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),    
    path('api/appointments/', AppointmentListView.as_view(), name='appointments'),
    path('api/appointments_all/', AppointmentAllView.as_view(), name='appointments_all'),
]
