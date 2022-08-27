from django.test import Client
from requests import Response

from airlines.models import Airplane


def test_airplanes_get(db, client: Client, airplane: Airplane) -> None:
    response: Response = client.get(path='/airplanes/')

    assert response.status_code == 200
    assert response.json() == [
        {
            'pk': 3,
            'passenger_capacity': 100,
            'consumption_per_minute': 1.0788898309344879,
            'max_flight_duration': 556.1272178089823
        }
    ]


def test_airplane_create(db, client: Client) -> None:
    response: Response = client.post(
        path='/airplanes/', data={'pk': 4, 'passenger_capacity': 200}
    )

    assert response.status_code == 201
    assert Airplane.objects.count() == 1

    airplane = Airplane.objects.last()
    assert airplane.plane_id == 4
    assert airplane.passenger_capacity == 200


def test_airplane_model(db, airplane: Airplane) -> None:
    assert airplane.fuel_tank_capacity == 600
    assert airplane.consumption_per_minute == 1.0788898309344879
    assert airplane.max_flight_duration == 556.1272178089823
