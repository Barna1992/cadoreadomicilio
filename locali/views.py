from .models import Locale, ComuneConsegna
from .serializers import LocaleSerializer, ComuneConsegnaSerializer
from rest_framework import generics

class LocaleList(generics.ListCreateAPIView):
    queryset = Locale.objects.all()
    serializer_class = LocaleSerializer

class ComuniList(generics.ListCreateAPIView):
    queryset = ComuneConsegna.objects.all()
    serializer_class = ComuneConsegnaSerializer
