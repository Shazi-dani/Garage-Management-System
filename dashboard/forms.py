from django import forms
from django.utils.safestring import mark_safe
from .models import Appointment, Vehicle
import base64


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user', 'vehicle', 'service', 'appointment_date', 'description']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# Need custom Vehicle model in order to show image field in views
class VehicleAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False)

    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ('image',)  # Exclude the binary image field

    def __init__(self, *args, **kwargs):
        super(VehicleAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.image:
            image_data = base64.b64encode(self.instance.image).decode('utf-8')
            self.fields['image_file'].help_text = mark_safe(
                f'<img src="data:image/jpeg;base64,{image_data}" width="150" height="150" />'
            )
    
    def save(self, commit=True):
        instance = super(VehicleAdminForm, self).save(commit=False)
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            instance.image = image_file.read()
        if commit:
            instance.save()
        return instance
