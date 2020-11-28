from config.views import Viewset
from .models import Contractor
from .serializers import ContractorSerializer


class ContractorAPIView(Viewset):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
