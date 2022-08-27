from pytest import fixture

from airlines.models import Airplane


@fixture
def airplane():
    return Airplane.objects.create(plane_id=3, passenger_capacity=100)
