from rest_framework import serializers
from .models import ExpectedArrival

class ExpectedArrivalSrializer(serializers.ModelSerializer):

    class Meta:
        model = ExpectedArrival
        fields = "__all__"
