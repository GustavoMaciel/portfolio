from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from main.models import Person, Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ContactSerializer(serializers.ModelSerializer):
    person = serializers.SerializerMethodField()
    class Meta:
        model = Contact
        fields = ['subject', 'received_from', 'received_email', 'message', 'date', 'person']

    def get_person(self, obj):
        if(obj.person != None):
            person = Person.objects.get(id=obj.person.id)
            serializer = PersonSerializer(person, read_only=True)
            return serializer.data
        else:
            return None

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer