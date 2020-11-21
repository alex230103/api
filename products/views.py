from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        pass
