from config.views import Viewset
from .serializers import ExpectedArrivalSrializer
from .models import ExpectedArrival

class ExpectedArrivalAPIView(Viewset):
    queryset = ExpectedArrival.objects.all()
    serializer_class = ExpectedArrivalSrializer
