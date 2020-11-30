from rest_framework import serializers
from .models import Product, Unit


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('name', 'ratio')


class ProductSerializer(serializers.ModelSerializer):
    base_unit = UnitSerializer(many=False, read_only=True)
    units = UnitSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return self.Meta.model.create_product(**validated_data)

    class Meta:
        model = Product
        fields = ('id', 'name', 'base_unit', 'units')
