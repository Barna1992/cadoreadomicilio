from rest_framework import serializers
from .models import Locale

class LocaleSerializer(serializers.ModelSerializer):
    categoria = serializers.SerializerMethodField()
    comune = serializers.SerializerMethodField()
    chiusura = serializers.SerializerMethodField()

    def get_categoria(self, instance):
        return instance.get_categoria_display()

    def get_comune(self, instance):
        return instance.get_comune_display()

    def get_chiusura(self, instance):
        return instance.get_chiusura_display()

    class Meta:
        model = Locale
        fields = ('__all__')
