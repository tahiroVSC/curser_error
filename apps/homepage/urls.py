from django.urls import path
from apps.homepage.views import HomePageViewAPI, HomePageDetailViewAPI

urlpatterns = [
    path('homepage/', HomePageViewAPI.as_view()),
    path('homepage/<int:id>/', HomePageDetailViewAPI.as_view()),
]