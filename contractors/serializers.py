from rest_framework import serializers
from .models import Contractor, CONTRACTOR_TYPES


class ContractorSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=CONTRACTOR_TYPES)

    class Meta:
        model = Contractor
        fields = ('id', 'name', 'type')
