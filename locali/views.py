from .models import Locale, ComuneConsegna
from .serializers import LocaleSerializer, ComuneConsegnaSerializer
from rest_framework import generics

class LocaleList(generics.ListCreateAPIView):
    queryset = Locale.objects.all()
    serializer_class = LocaleSerializer

class ComuniList(generics.ListCreateAPIView):
    queryset = sorted(ComuneConsegna.objects.all(), key= lambda t: t.get_comune_display())
    serializer_class = ComuneConsegnaSerializer
