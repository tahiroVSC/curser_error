from django.urls import path
from apps.contacts.views import ContactRetrieveAPIView, ContactListAPIView

urlpatterns = [
    path('contacts/', ContactListAPIView.as_view()),
    path('contacts/<int:pk>/', ContactRetrieveAPIView.as_view()),
]
