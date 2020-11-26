from django.urls import path, include
from .views import ProductAPIView
from rest_framework.routers import DefaultRouter

product_router = DefaultRouter()
product_router.register(r'products', ProductAPIView)
