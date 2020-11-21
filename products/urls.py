from django.urls import path, include
from .views import ProductAPIView
urlpatterns = [
    path('', ProductAPIView.as_view())
]
