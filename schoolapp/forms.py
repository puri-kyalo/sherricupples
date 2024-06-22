from django import forms
from schoolapp.models import ContactSubmission, AppointmentSubmission


class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject',  'message']

class AppointmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AppointmentSubmission
        fields = ['name', 'email', 'name', 'age',  'message']
