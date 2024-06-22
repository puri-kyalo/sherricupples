from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class AppointmentSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
