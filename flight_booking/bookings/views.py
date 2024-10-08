
# bookings/views.py
from django.shortcuts import render, redirect
from .forms import BookingForm  # Import your form
from .models import Booking


def booking_form_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            # Create a new Booking object but don't save it yet
            booking = form.save(commit=False)
            booking.save()  # Save to the database
            return redirect('/success/')  # Redirect to a success page after submission
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form})  # Render the template


def success(request):
    return render(request, 'bookings/success.html')  # Render the success page
