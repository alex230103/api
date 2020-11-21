from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

