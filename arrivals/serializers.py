from rest_framework import serializers
from .models import ExpectedArrival, ExpectedArrivalEntry

class ExpectedArrivalSrializer(serializers.ModelSerializer):

    class Meta:
        model = ExpectedArrival
        fields = "__all__"


class ExpectedArrivalEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpectedArrivalEntry
        fields = "__all__"
