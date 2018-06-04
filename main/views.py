from django.shortcuts import render
from django.views import View
from django.contrib import messages
from main.forms import ContactForm
from main.models import Person, Contact

# Create your views here.


class Home(View):
    lang = None

    def get(self, request):
        if(self.lang == "pt-br"):
            return render(request, 'pt-br/index.html')
        return render(request, 'index.html')

class Contact(View):
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
            contact = form.save()
            email = form.cleaned_data['received_email']
            name = form.cleaned_data['received_from']

            try:
                person = Person.objects.get(email=email)
            except Person.DoesNotExist:
                person = Person(name=name, email=email)
                person.save()

            person.contact_made.add(contact)
            person.save()

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
