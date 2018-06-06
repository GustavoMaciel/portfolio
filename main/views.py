from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from main.models import Person, Contact
from django.http import HttpResponse
import requests

# Create your views here.

class Home(View):
    def get_persons(self):
        data = requests.get('http://gustavo-nunes.tk/rest/person/')
        persons = data.json()
        for person in persons:
            try:
                Person.objects.get(email=person['email'])
            except Person.DoesNotExist:
                current = Person(name=person['name'], email=person['email'], date_joined=person['date_joined'])
                current.save()

    def get_contacts(self):
        data = requests.get('http://gustavo-nunes.tk/rest/contact/')
        contacts = data.json()
        for contact in contacts:
            try:
                Contact.objects.get(subject=contact['subject'], received_from=contact['received_from'],
                                  received_email=contact['received_email'], message=contact['message'], date=contact['date'])
            except Contact.DoesNotExist:
                if(contact['person'] != None):
                    person = Person.objects.get(pk=contact['person']['id'])
                else:
                    person = None
                current = Contact(subject=contact['subject'], received_from=contact['received_from'],
                                  received_email=contact['received_email'], message=contact['message'], date=contact['date'],
                                  person=person)
                current.save()
    #
    # def get_contacts(self):
    #     data = requests.get('http://localhost:8001/rest/user/')
    #     persons = data.json()
    #     for person in persons:
    #         try:
    #             Person.objects.get(email=person.email)
    #         except Person.DoesNotExist:
    #             current = Person(name=person.name, email=person.email, date_joined=person.date_joined)
    #             current.save()

    def get(self, request):
        self.get_persons()
        self.get_contacts()

        persons = Person.objects.all()
        contacts = Contact.objects.all()

        context = {'persons': persons,
                   'contacts': contacts}

        return render(request, 'teste.html', context=context)