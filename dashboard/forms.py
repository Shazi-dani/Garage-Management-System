from django import forms
from django.utils.safestring import mark_safe
from .models import Appointment, Vehicle, Inquiry
import base64


class AppointmentForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Appointment instances.

    Attributes:
        Meta:
            model (Model): The model class this form is linked to.
            fields (list): List of model fields included in the form.
            widgets (dict): Custom widgets to use in the form for specific fields.
    """

    class Meta:
        model = Appointment
        fields = ["user", "vehicle", "service", "appointment_date", "description"]
        widgets = {
            "appointment_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


# Need custom Vehicle model in order to show image field in views
class VehicleAdminForm(forms.ModelForm):
    """
    A custom ModelForm for Vehicle to handle image uploads via a file field instead of directly handling binary data.

    This form includes a FileField for uploading images and excludes the original binary image field in the model.
    It also displays a preview of the current image if it exists.

    Attributes:
        image_file (FileField): A field for uploading an image file, not required.

    Methods:
        __init__: Customizes initialization to possibly include an image preview.
        save: Overrides the default save method to handle image file saving.
    """

    image_file = forms.FileField(required=False)

    class Meta:
        model = Vehicle
        fields = "__all__"
        exclude = ("image",)  # Exclude the binary image field

    def __init__(self, *args, **kwargs):
        super(VehicleAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.image:
            image_data = base64.b64encode(self.instance.image).decode("utf-8")
            self.fields["image_file"].help_text = mark_safe(
                f'<img src="data:image/jpeg;base64,{image_data}" width="150" height="150" />'
            )

    def save(self, commit=True):
        """
        Saves the form instance and handles the uploaded image file, saving it in binary format if provided.

        Args:
            commit (bool): Whether to save the instance to the database immediately.

        Returns:
            instance (Vehicle): The saved Vehicle model instance, with image data updated if provided.
        """
        instance = super(VehicleAdminForm, self).save(commit=False)
        image_file = self.cleaned_data.get("image_file")
        if image_file:
            instance.image = image_file.read()
        if commit:
            instance.save()
        return instance


# Custom Model to Save User inquiries in a database
class InquiryForm(forms.ModelForm):
    """
    A ModelForm for creating Inquiry instances, capturing various user inputs like name, email, and message.

    Attributes:
        Meta:
            model (Model): The model class this form is linked to.
            fields (list): List of model fields included in the form.
    """

    class Meta:
        model = Inquiry
        fields = ["first_name", "last_name", "email", "subject", "message"]
