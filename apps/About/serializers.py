from rest_framework import serializers
from apps.About.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields  = ('title', 'desc', 'image' )
