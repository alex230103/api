from django.contrib import admin
from django.urls import path, include


patterns_api = [
    path('products/', include('products.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))
]
