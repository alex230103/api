from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from products.urls import product_router

urlpatterns = [
    path('admin/', admin.site.urls),


]

urlpatterns += product_router.urls
