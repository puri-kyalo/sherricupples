from django.contrib import admin
from schoolapp.models import ContactSubmission, AppointmentSubmission

# Register your models here.
admin.site.register(ContactSubmission)
admin.site.register(AppointmentSubmission)