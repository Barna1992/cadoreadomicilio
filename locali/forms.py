from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import Locale
from cadoreadomicilio import settings

class LocaleForm(forms.ModelForm):

    class Meta:
        model = Locale
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome del locale"
        self.fields['come_funziona'].label = "Modalità di consegna / ritiro"
        self.fields['pranzo'].label = "Consegni a pranzo ?"
        self.fields['cena'].label = "Consegni a cena ?"

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['name'] = cleaned_data['name'].capitalize()
        try:
            subject = 'Locale inserito'
            text = render_to_string('locali/email.html', {'cleaned_data': cleaned_data})
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['andrea.barnabo92@gmail.com',]
            email = EmailMessage(subject, text, email_from, recipient_list)
            email.content_subtype = "html"
            email.send()
        except:
            pass    
        return cleaned_data
