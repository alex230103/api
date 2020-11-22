from django.urls import path, include
from .views import ProductAPIView

product_list = ProductAPIView.as_view({
    'get': 'list',
    'post': 'create'
})

product_retrieve = ProductAPIView.as_view({
    'get': 'retrieve',
    'put': 'update'
})

product_units = ProductAPIView.as_view({
    'get': 'product_units',
    'post': 'create_unit'
})

urlpatterns = [
    path('', product_list),
    path('<int:pk>/', product_retrieve),
    path('<int:pk>/units/', product_units),
]
