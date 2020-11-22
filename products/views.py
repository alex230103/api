from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer, UnitSerializer
from rest_framework.response import Response

class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def product_units(self, request, pk=None):
        product = self.get_object()
        units = product.units
        unit_serializer = UnitSerializer(units, many=True)
        return Response(unit_serializer.data)
