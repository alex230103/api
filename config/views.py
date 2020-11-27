from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

class Viewset(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass

