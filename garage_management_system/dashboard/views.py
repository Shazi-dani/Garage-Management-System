from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.utils.timezone import now

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Appointment
from .forms import AppointmentForm
from .serializers import AppointmentSerializer

# Create your views here.
User = get_user_model()

class DashboardView(TemplateView, APIView):
    template_name = 'dashboard.html'
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            user_type = getattr(user, 'user_type', 'customer')
            username = user.username
        else:
            user_type = 'guest'
            username = 'Guest'

        print("Found User: ", self.request.user.username)
        # Get current month appointments
        current_month = now().month
        current_year = now().year
        appointments = Appointment.objects.filter(
            appointment_date__year=current_year,
            appointment_date__month=current_month
        )

        # Data for chart
        chart_data = []
        for appointment in appointments:
            chart_data.append({
                'name': appointment.user.username,
                'datetime': appointment.appointment_date.strftime("%Y-%m-%d %H:%M:%S"),
            })

        # Appointments list based on user type
        if user.is_authenticated and user_type in ['technician', 'admin']:
            user_appointments = appointments
        elif user.is_authenticated and user_type == 'customer':
            user_appointments = appointments.filter(user=user)
        else:
            user_appointments = []

        context.update({
            'chart_data': chart_data,
            'user_appointments': user_appointments,
            'user_type': user_type,
            'username': username,
        })

        return context

    def post(self, request, *args, **kwargs):
        if 'mark_done' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.status = 'done'
            appointment.save()
            return redirect('dashboard')

        if request.content_type == 'application/json':
            serializer = AppointmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return redirect('dashboard')

    def get(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            current_month = now().month
            current_year = now().year
            appointments = Appointment.objects.filter(
                appointment_date__year=current_year,
                appointment_date__month=current_month
            )

            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)

        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            self.authentication_classes = [JWTAuthentication]
            self.permission_classes = [AllowAny]
            return APIView.dispatch(self, request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'create_appointment.html'
    success_url = reverse_lazy('success_url')  # Replace with your success URL

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'edit_appointment.html'
    success_url = reverse_lazy('success_url')  # Replace with your success URL

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'confirm_delete_appointment.html'
    success_url = reverse_lazy('success_url')  # Replace with your success URL

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'

# DRF API views
class AppointmentCreateAPIView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDeleteAPIView(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer