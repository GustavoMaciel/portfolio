from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):
    subject = forms.CharField(
        label='Subject'
    )
    received_from = forms.CharField(
        label='Your Name'
    )
    received_email = forms.CharField(
        label='Your Email:'
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Message'
    )

    class Meta:
        model = Contact
        fields = ['subject', 'received_from', 'received_email', 'message', ]
