from rest_framework import serializers
from .models import ExpectedArrival

class ExpectedArrivalSrializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d-%m-%YT%H:%M:%S")
    kis_date = serializers.DateTimeField(format="%d-%m-%YT%H:%M:%S")

    class Meta:
        model = ExpectedArrival
        fields = "__all__"
