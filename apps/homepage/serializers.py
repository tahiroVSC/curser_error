from rest_framework import serializers
from apps.homepage.models import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields  = ('subtitle','title', 'photo')
