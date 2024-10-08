# bookings/models.py
from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)  # Adjust length as needed
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    po_box = models.CharField(max_length=100, blank=True)  # Optional field
    emergency_phone = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=50)
    visa_document = models.FileField(upload_to='visa_documents/', blank=True)  # Optional field
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
