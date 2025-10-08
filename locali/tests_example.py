"""
Test di esempio per l'app locali.
Rinomina questo file in tests.py per attivarli.

Per eseguire:
    python manage.py test locali

Per eseguire con pytest (opzionale):
    pytest locali/tests.py
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Locale, ComuneConsegna


class ComuneConsegnaModelTest(TestCase):
    """Test per il model ComuneConsegna"""

    def setUp(self):
        self.comune = ComuneConsegna.objects.create(comune='1')

    def test_comune_creation(self):
        """Test creazione comune"""
        self.assertEqual(ComuneConsegna.objects.count(), 1)
        self.assertEqual(self.comune.comune, '1')

    def test_comune_str_representation(self):
        """Test rappresentazione stringa"""
        self.assertEqual(str(self.comune), 'Auronzo di Cadore (BL)')


class LocaleModelTest(TestCase):
    """Test per il model Locale"""

    def setUp(self):
        self.comune_consegna = ComuneConsegna.objects.create(comune='1')
        self.locale = Locale.objects.create(
            name="Bar Test",
            comune='1',
            email="test@example.com",
            telefono="0435 123456",
            pranzo=True,
            cena=False,
            categoria='BA',
            chiusura='LU'
        )
        self.locale.consegno_a.add(self.comune_consegna)

    def test_locale_creation(self):
        """Test creazione locale"""
        self.assertEqual(Locale.objects.count(), 1)
        self.assertEqual(self.locale.name, "Bar Test")

    def test_locale_str_representation(self):
        """Test rappresentazione stringa"""
        expected = "Bar Test - Auronzo di Cadore (BL)"
        self.assertEqual(str(self.locale), expected)

    def test_locale_ordering(self):
        """Test ordinamento locali per nome"""
        Locale.objects.create(
            name="Zzz Ultimo",
            comune='1',
            pranzo=False,
            cena=False,
            categoria='AL',
            chiusura='DO'
        )
        Locale.objects.create(
            name="Aaa Primo",
            comune='1',
            pranzo=False,
            cena=False,
            categoria='AL',
            chiusura='DO'
        )

        locali = Locale.objects.all()
        self.assertEqual(locali[0].name, "Aaa Primo")
        self.assertEqual(locali[2].name, "Zzz Ultimo")

    def test_telefono_validation_valid(self):
        """Test validazione telefono con formato valido"""
        locale = Locale(
            name="Test",
            comune='1',
            telefono="0435 123456",
            pranzo=False,
            cena=False,
            categoria='AL',
            chiusura='DO'
        )
        try:
            locale.full_clean()  # Valida tutti i campi
        except ValidationError:
            self.fail("Validazione fallita per telefono valido")

    def test_telefono_validation_with_prefix(self):
        """Test validazione telefono con prefisso internazionale"""
        locale = Locale(
            name="Test",
            comune='1',
            telefono="+39 0435 123456",
            pranzo=False,
            cena=False,
            categoria='AL',
            chiusura='DO'
        )
        try:
            locale.full_clean()
        except ValidationError:
            self.fail("Validazione fallita per telefono con prefisso")

    def test_telefono_validation_invalid(self):
        """Test validazione telefono con formato invalido"""
        locale = Locale(
            name="Test",
            comune='1',
            telefono="123",  # Troppo corto
            pranzo=False,
            cena=False,
            categoria='AL',
            chiusura='DO'
        )
        with self.assertRaises(ValidationError):
            locale.full_clean()


class LocaleAPITest(APITestCase):
    """Test per l'API REST dei locali"""

    def setUp(self):
        self.comune = ComuneConsegna.objects.create(comune='1')
        self.locale = Locale.objects.create(
            name="API Test Locale",
            comune='1',
            email="api@test.com",
            telefono="0435 111111",
            pranzo=True,
            cena=True,
            categoria='RI',
            chiusura='MA'
        )
        self.locale.consegno_a.add(self.comune)

    def test_get_locali_list(self):
        """Test GET /api/locali/ restituisce lista"""
        response = self.client.get('/api/locali/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Con paginazione, i risultati sono in 'results'
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_locali_pagination(self):
        """Test paginazione API"""
        # Crea 25 locali per testare paginazione (PAGE_SIZE=20)
        for i in range(25):
            Locale.objects.create(
                name=f"Locale {i}",
                comune='1',
                pranzo=False,
                cena=False,
                categoria='AL',
                chiusura='DO'
            )

        response = self.client.get('/api/locali/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('count', response.data)
        self.assertEqual(response.data['count'], 26)  # 25 + 1 dal setUp
        self.assertIn('next', response.data)
        self.assertIsNotNone(response.data['next'])

    def test_get_comuni_list(self):
        """Test GET /api/comuni/ restituisce lista"""
        response = self.client.get('/api/comuni/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_api_rate_limiting(self):
        """
        Test rate limiting API (questo test richiede configurazione specifica)
        Commentato perché potrebbe essere lento
        """
        # for i in range(101):  # Supera il limite di 100/hour
        #     response = self.client.get('/api/locali/')
        #
        # # Dopo 100 richieste, dovremmo ricevere 429 Too Many Requests
        # self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        pass


class LocaleFormTest(TestCase):
    """Test per LocaleForm"""

    def test_form_valid_data(self):
        """Test form con dati validi"""
        from .forms import LocaleForm

        comune = ComuneConsegna.objects.create(comune='1')

        form_data = {
            'name': 'form test',
            'comune': '1',
            'email': 'form@test.com',
            'telefono': '0435 222222',
            'pranzo': True,
            'cena': False,
            'categoria': 'PI',
            'chiusura': 'LU',
            'consegno_a': [comune.id]
        }

        form = LocaleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_name_capitalization(self):
        """Test che il form capitalizzi il nome"""
        from .forms import LocaleForm

        comune = ComuneConsegna.objects.create(comune='1')

        form_data = {
            'name': 'pizzeria da mario',  # lowercase
            'comune': '1',
            'pranzo': False,
            'cena': True,
            'categoria': 'PI',
            'chiusura': 'LU',
            'consegno_a': [comune.id]
        }

        form = LocaleForm(data=form_data)
        if form.is_valid():
            cleaned = form.clean()
            self.assertEqual(cleaned['name'], 'Pizzeria da mario')  # Capitalize


# Test di integrazione (esempi)

class IntegrationTest(TestCase):
    """Test di integrazione end-to-end"""

    def test_create_locale_via_form_view(self):
        """Test creazione locale tramite view"""
        comune = ComuneConsegna.objects.create(comune='1')

        form_data = {
            'name': 'Integration Test',
            'comune': '1',
            'email': 'integration@test.com',
            'telefono': '0435 333333',
            'pranzo': True,
            'cena': True,
            'categoria': 'RI',
            'chiusura': 'MA',
            'consegno_a': [comune.id]
        }

        response = self.client.post('/create/', form_data, follow=True)

        # Verifica redirect su successo
        self.assertEqual(response.status_code, 200)

        # Verifica che il locale sia stato creato
        self.assertTrue(
            Locale.objects.filter(name='Integration Test').exists()
        )


# Istruzioni per eseguire i test:
"""
# Test singolo
python manage.py test locali.tests.LocaleModelTest

# Test singolo metodo
python manage.py test locali.tests.LocaleModelTest.test_locale_creation

# Tutti i test dell'app
python manage.py test locali

# Con verbose output
python manage.py test locali --verbosity=2

# Con pytest (se installato)
pytest locali/tests.py -v
pytest locali/tests.py::LocaleModelTest -v
pytest locali/tests.py -k "telefono" -v  # Solo test che contengono "telefono"
"""
