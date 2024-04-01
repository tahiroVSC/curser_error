from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.Offering.models import Offering
from apps.Offering.serializers import OfferingSerializer
    
    # Create your views here.
class OfferingAPIViews(ListAPIView):
    queryset = Offering.objects.all()[:10]
    serializer_class = OfferingSerializer

   
# class OfferingDetailViewAPI(RetrieveAPIView):
#     queryset = Offering.objects.all()
#     serializer_class = OfferingDetailSerializer
#     lookup_field = 'id'