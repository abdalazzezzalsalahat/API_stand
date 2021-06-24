from rest_framework import serializers
from .models import Skyscraper

class SkyscraperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skyscraper
        fields = ('__all__')
        