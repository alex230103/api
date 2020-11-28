from django.contrib import admin
from django.urls import path, include
from products.urls import product_router
from rest_framework.schemas import get_schema_view


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(
        title="WMS Service",
        description="API for developers wms service"
    ), name='wms-schema'),


]

urlpatterns += product_router.urls
