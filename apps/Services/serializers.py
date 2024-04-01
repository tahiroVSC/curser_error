from rest_framework import serializers
from apps.Services.models import Services


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields  = ('title','note','hours_week','price')