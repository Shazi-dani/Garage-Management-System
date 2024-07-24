from django.contrib import admin
from .models import Vehicle, Service, Appointment
from .forms import VehicleAdminForm


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Vehicle model entries.

    Attributes:
        form (ModelForm): Specifies the custom form to use for the Vehicle model.
        list_display (list): Defines the fields that will be displayed on the model's list page.
        search_fields (list): Specifies the fields that should be searchable in the admin list view.
        list_filter (list): Defines the fields that will be used for filtering in the list view.
        fields (tuple): Specifies the fields to be included in the form view of the model.
    """
    form = VehicleAdminForm
    list_display = ['make', 'model', 'color', 'license_plate_no', 'vehicle_number', 'vehicle_type', 'owner']
    search_fields = ['make', 'model', 'license_plate_no', 'vehicle_number']
    list_filter = ['make', 'model', 'vehicle_type', 'color']
    fields = ('model', 'make', 'color', 'license_plate_no', 'vehicle_number', 'vehicle_type', 'owner', 'description', 'image_file')  # Use image_file

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Service model entries.

    Attributes:
        list_display (list): Defines the fields that will be displayed on the model's list page.
        search_fields (list): Specifies the fields that should be searchable in the admin list view.
        list_filter (list): Defines the fields that will be used for filtering in the list view.
    """
    list_display = ['description', 'cost']
    search_fields = ['description']
    list_filter = ['cost']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Appointment model entries.

    Attributes:
        list_display (list): Defines the fields that will be displayed on the model's list page.
        search_fields (list): Specifies the fields that should be searchable in the admin list view.
        list_filter (list): Defines the fields that will be used for filtering in the list view.
    """
    list_display = ['user', 'vehicle', 'service']
    search_fields = ['user__username', 'vehicle__license_plate_no', 'service__description']
    list_filter = ['service', 'vehicle__make', 'vehicle__model']
