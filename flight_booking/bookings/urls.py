# bookings/urls.py
from django.urls import path
from .views import booking_form_view
from django.conf import settings
from django.conf.urls.static import static
from bookings import views

urlpatterns = [
    path('', booking_form_view, name='booking_form'),
    path('success/', views.success, name='success'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


