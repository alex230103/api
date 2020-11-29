from config.views import Viewset
from .serializers import ExpectedArrivalSrializer, ExpectedArrivalEntrySerializer
from .models import ExpectedArrival
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ExpectedArrivalAPIView(Viewset):
    queryset = ExpectedArrival.objects.all()
    serializer_class = ExpectedArrivalSrializer

    def get_serializer_class(self):
        actions = {
            "add_entry": ExpectedArrivalEntrySerializer
        }
        return actions.get(self.action, self.serializer_class)

    @action(detail=True, methods=['GET'])
    def enries(self, request, pk=None):
        arrival = self.get_object()
        entries = arrival.entry
        serializer = ExpectedArrivalEntrySerializer(entries, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def add_entry(self, request, pk=None):
        arrival = self.get_object()
        serializer = self.get_serializer_class()
        entry = serializer(data=request.data)
        if entry.is_valid():
            entry.save(expected_arrival=arrival)
            
            return Response(entry.data)

        
        return Response({"message":"not valid"}, status=status.HTTP_400_BAD_REQUEST)
