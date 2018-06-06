from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from main.forms import ContactForm
from main.models import Person, Contact

# Create your views here.


class Home(View):
    lang = None

    def get(self, request):
        if(self.lang == "pt-br"):
            return render(request, 'pt-br/index.html')
        return render(request, 'index.html')

class ContactView(View):
    lang = None

    def get(self, request):
        form = ContactForm()
        context = {'form': form}

        if(self.lang == 'pt-br'):
            return render(request, 'pt-br/contact.html', context)
        return render(request, 'contact.html', context)

    def post(self, request):
        form = ContactForm(request.POST)

        if(form.is_valid()):
            email = form.cleaned_data['received_email']
            name = form.cleaned_data['received_from']

            try:
                person = Person.objects.get(email=email)
            except Person.DoesNotExist:
                person = Person(name=name, email=email)
                person.save()

            contact = form.save()
            contact.person = person
            contact.save()



            if(self.lang == 'pt-br'):
                succes = 'Obrigado por entrar em contato! ;)'
            else:
                succes = 'Thank you for reaching out! ;)'

            messages.success(request, succes)
            form = ContactForm()
            context = {'form': form}
            return render(request, 'contact.html', context)

        else:

            if(self.lang == 'pt-br'):
                error = 'Não foi possível registrar seu contato, por favor mantenha em mente que todos os campos são' \
                        ' obrigatórios.'
            else:
                error = "It wasn't possible to register your contact, please make note that all fields are required."

            messages.error(request, error)
            context = {'form': form}
            return render(request, 'contact.html', context)


## REST FRAMEWORK

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from main.models import Person, Contact
from main.serializers import PersonSerializer, ContactSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'persons': reverse('person-list', request=request, format=format),
        'contacts': reverse('contact-list', request=request, format=format),
    })


class UserList(APIView):
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonList(APIView):
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

class PersonDetail(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk=pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ContactList(APIView):
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

class ContactDetail(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contact = self.get_object(pk=pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)