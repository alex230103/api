from config.views import Viewset
from .models import Product
from .serializers import ProductSerializer, UnitSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductAPIView(Viewset):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        units_actions = {
            'create_unit': UnitSerializer
        }

        return units_actions.get(self.action, ProductSerializer)
    
    @action(detail=True)
    def units(self, request, pk=None):
        product = self.get_object()
        units = product.units
        unit_serializer = UnitSerializer(units, many=True)
        return Response(unit_serializer.data)


    @action(detail=True, methods=['POST'])
    def create_unit(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer_class()
        unit_serializer = serializer(data=request.data)
        if unit_serializer.is_valid(raise_exception=True):
            unit = product.create_unit(**unit_serializer.data)
            return Response(serializer(unit).data)
