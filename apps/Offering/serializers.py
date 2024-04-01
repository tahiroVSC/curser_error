from rest_framework import serializers
from apps.Offering.models import Offering, Icons

class IconsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Icons
        fields = ('icon', 'image_url')

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

class OfferingSerializer(serializers.ModelSerializer):
    image = IconsSerializer()

    class Meta:
        model = Offering
        fields = ('id', 'title_ru', 'title_ky', 'image', 'hide')
