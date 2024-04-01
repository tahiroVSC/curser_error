from django.urls import path
from apps.schedule.views import ScheduleRetrieveAPIView, ScheduleListAPIView

urlpatterns = [
    path('schedule/', ScheduleListAPIView.as_view()),
    path('schedule/<int:pk>/', ScheduleRetrieveAPIView.as_view()),
]
