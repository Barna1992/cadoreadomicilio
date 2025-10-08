import logging
from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import Locale, ComuneConsegna
from cadoreadomicilio import settings

# Configurazione logging
logger = logging.getLogger(__name__)

class LocaleForm(forms.ModelForm):

    class Meta:
        model = Locale
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome del locale"
        self.fields['come_funziona'].label = "Modalità di consegna / ritiro"
        self.fields['pranzo'].label = "Consegni a pranzo?"
        self.fields['cena'].label = "Consegni a cena?"
        comuni_consegna = sorted(ComuneConsegna.objects.all(), key= lambda t: t.get_comune_display())
        self.fields['consegno_a'].choices = [( comune.id, comune.get_comune_display() ) for comune in comuni_consegna]

    def clean(self):
        cleaned_data = super().clean()

        # Capitalizza il nome del locale
        if 'name' in cleaned_data and cleaned_data['name']:
            cleaned_data['name'] = cleaned_data['name'].capitalize()

        # Invia notifica email all'admin
        try:
            subject = 'Nuovo locale inserito - Cadore a Domicilio'
            text = render_to_string('locali/email.html', {'cleaned_data': cleaned_data})
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.ADMIN_EMAIL]

            email = EmailMessage(subject, text, email_from, recipient_list)
            email.content_subtype = "html"
            email.send()

            logger.info(f"Email di notifica inviata con successo per il locale: {cleaned_data.get('name', 'N/A')}")

        except Exception as e:
            # Log dell'errore invece di ignorarlo silenziosamente
            logger.error(f"Errore nell'invio dell'email di notifica: {str(e)}")
            # Non blocchiamo la creazione del locale se l'email fallisce
            # ma l'errore è tracciato nei log

        return cleaned_data
