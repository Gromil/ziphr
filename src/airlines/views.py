from rest_framework.viewsets import ModelViewSet

from airlines.models import Airplane
from airlines.serializers import AirplaneSerializer


class AirplanesViewSet(ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
