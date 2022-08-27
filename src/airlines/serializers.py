from rest_framework.serializers import ModelSerializer

from airlines.models import Airplane


class AirplaneSerializer(ModelSerializer):
    class Meta:
        model = Airplane
        fields = (
            'pk',
            'passenger_capacity',
            'consumption_per_minute',
            'max_flight_duration'
        )
