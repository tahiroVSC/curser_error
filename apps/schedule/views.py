from rest_framework.generics import RetrieveAPIView, ListAPIView
from apps.schedule.serializers import ScheduleSerializer
from apps.schedule.models import Schedule


class ScheduleListAPIView(ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleRetrieveAPIView(RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
