from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter

from products.views import ProductAPIView
from contractors.views import ContractorAPIView

router = DefaultRouter()

router.register(r'products', ProductAPIView)
router.register(r'contractors', ContractorAPIView)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(
        title="WMS Service",
        description="API for developers wms service"
    ), name='wms-schema'),


]

urlpatterns += router.urls