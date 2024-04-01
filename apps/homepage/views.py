
from apps.homepage.models import HomePage
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.homepage.serializers import HomePageSerializer


class HomePageViewAPI(ListAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer


class HomePageDetailViewAPI(RetrieveAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    lookup_field = 'id'
# Create your views here.
