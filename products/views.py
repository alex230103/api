from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer, UnitSerializer
from rest_framework.response import Response

class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        units_actions = {
            'create_unit': UnitSerializer
        }

        return units_actions.get(self.action, ProductSerializer)

    def product_units(self, request, pk=None):
        product = self.get_object()
        units = product.units
        unit_serializer = UnitSerializer(units, many=True)
        return Response(unit_serializer.data)


    def create_unit(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer_class()
        unit_serializer = serializer(data=request.data)
        if unit_serializer.is_valid(raise_exception=True):
            unit = product.create_unit(**unit_serializer.data)
            return Response(serializer(unit).data)
