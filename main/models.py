from django.db import models

# Create your models here.

class Contact(models.Model):
    subject = models.CharField(max_length=254, blank=False, null=True)
    received_from = models.CharField(max_length=254, blank=False, null=True)
    received_email = models.EmailField(max_length=254, blank=False, null=True)
    message = models.TextField(blank=False, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Person(models.Model):
    name = models.CharField(max_length=254, blank=False, null=True)
    email = models.EmailField(max_length=254, blank=False, null=True)
    contact_made = models.ManyToManyField(Contact, related_name='contact')
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
