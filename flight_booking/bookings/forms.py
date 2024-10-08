# bookings/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'  # to include all fields in the form
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'visa_document': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }
