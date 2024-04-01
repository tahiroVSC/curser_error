from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields  = ('first_number', 'second_number', 'email', 'address', 'links')
