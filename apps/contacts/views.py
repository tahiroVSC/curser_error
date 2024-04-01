from rest_framework.generics import RetrieveAPIView, ListAPIView
from apps.contacts.serializers import ContactSerializer
from apps.contacts.models import Contact


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
