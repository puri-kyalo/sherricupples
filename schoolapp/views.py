from django.shortcuts import render, redirect
from django.urls import reverse
from schoolapp.forms import  ContactSubmissionForm, AppointmentSubmissionForm


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def programmes(request):
    return render(request,'programmes.html')

def facts(request):
    return render(request,'facts.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def gallery(request):
    return render(request,'gallery.html')

def sports(request):
    return render(request,'sports.html')


def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('appointment_success'))  # Redirect to a success page or back to the contact page
    else:
        form = AppointmentSubmissionForm()
    return render(request, 'appointment.html', {'form': form})


def appointment_success_view(request):
    return render(request, 'appointment_success.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contact_success'))  # Redirect to a success page or back to the contact page
    else:
        form = ContactSubmissionForm()
    return render(request, 'contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'contact_success.html')
