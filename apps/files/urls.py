from django.urls import path
from apps.files.views import FileView


urlpatterns = [
    path('file/', FileView.as_view(),)
    ]
