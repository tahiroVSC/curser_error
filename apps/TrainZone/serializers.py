from rest_framework import serializers

from .models import TrainZone, TrainZoneImage

class TrainZoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainZoneImage
        fields = ('images',)  # Измените поля по необходимости

class TrainZoneSerializer(serializers.ModelSerializer):
    images = TrainZoneImageSerializer(many=True, read_only=True)

    class Meta:
        model = TrainZone
        fields = ('title', 'description', 'images', 'section')
