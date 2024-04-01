from rest_framework import serializers
from apps.Review.models import Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields  = ('photo', 'name', 'jobtitle','description')