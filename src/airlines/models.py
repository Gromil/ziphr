import math

from django.db import models


class Airplane(models.Model):
    DEFAULT_FUEL_CAPACITY = 200
    CAPACITY_INCREASE_PER_PASSENGER = 0.002

    passenger_capacity = models.IntegerField()
    plane_id = models.IntegerField(primary_key=True, unique=True)

    @property
    def fuel_tank_capacity(self) -> int:
        return self.pk * self.DEFAULT_FUEL_CAPACITY

    @property
    def consumption_per_minute(self) -> float:
        """returns value in liter per minute"""
        return (
            math.log(self.pk) * 0.8
            + self.passenger_capacity * self.CAPACITY_INCREASE_PER_PASSENGER
        )

    @property
    def max_flight_duration(self) -> float:
        """returns value in minutes"""
        return self.fuel_tank_capacity / self.consumption_per_minute
