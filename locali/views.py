from .models import Locale
from .serializers import LocaleSerializer
from rest_framework import generics

class LocaleList(generics.ListCreateAPIView):
    queryset = Locale.objects.all()
    serializer_class = LocaleSerializer
