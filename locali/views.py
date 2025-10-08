from .models import Locale, ComuneConsegna
from .serializers import LocaleSerializer, ComuneConsegnaSerializer
from rest_framework import generics

class LocaleList(generics.ListCreateAPIView):
    """
    API endpoint per listare e creare locali.
    Supporta paginazione e ordinamento per nome.
    """
    queryset = Locale.objects.all().select_related().prefetch_related('consegno_a')
    serializer_class = LocaleSerializer

class ComuniList(generics.ListCreateAPIView):
    """
    API endpoint per listare i comuni di consegna.
    Ottimizzato con ordinamento a livello database.
    """
    # Invece di usare sorted() in Python, ordiniamo a livello database
    queryset = ComuneConsegna.objects.all().order_by('comune')
    serializer_class = ComuneConsegnaSerializer
