from django.contrib import admin
from .models import Vehicle, Service, Appointment
from .forms import VehicleAdminForm


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    form = VehicleAdminForm
    list_display = ['make', 'model', 'color', 'license_plate_no', 'vehicle_number', 'vehicle_type', 'owner']
    search_fields = ['make', 'model', 'license_plate_no', 'vehicle_number']
    list_filter = ['make', 'model', 'vehicle_type', 'color']
    fields = ('model', 'make', 'color', 'license_plate_no', 'vehicle_number', 'vehicle_type', 'owner', 'description', 'image_file')  # Use image_file

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['description', 'cost']
    search_fields = ['description']
    list_filter = ['cost']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'vehicle', 'service']
    search_fields = ['user__username', 'vehicle__license_plate_no', 'service__description']
    list_filter = ['service', 'vehicle__make', 'vehicle__model']
