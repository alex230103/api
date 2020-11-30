from rest_framework import serializers
from .models import ExpectedArrival, ExpectedArrivalEntry
from products.serializers import ProductSerializer

class ExpectedArrivalSrializer(serializers.ModelSerializer):

    class Meta:
        model = ExpectedArrival
        fields = "__all__"


class ExpectedArrivalEntrySerializer(serializers.ModelSerializer):
    expected_arrival = ExpectedArrivalSrializer(read_only=True, many=False)
    product = ProductSerializer(read_only=True, many=False)

    class Meta:
        model = ExpectedArrivalEntry
        fields = ("id", "expected_arrival", "product", "quantity")
