from logistics_fleet.truck import Truck
from models.package import Package

class Actros(Truck):

    CAPACITY = 26000
    MAX_RANGE = 13000
    TRUCK_ID_RANGE = range(1026, 1040 + 1)
    UNIQUE_TRUCK_ID = 1026

    def __init__(self, truck_id: int, truck_type, enrolled_to_location):
        super().__init__(truck_id, truck_type, enrolled_to_location)
        self.capacity = Actros.CAPACITY

    @classmethod
    def unenroll_actors(cls):
        return Truck.unenroll_trucks(Actros.TRUCK_ID_RANGE, Actros.UNIQUE_TRUCK_ID)

    # @property
    # def remaining_capacity(self):
    #     return Actros.CAPACITY
    #
    # @remaining_capacity.setter
    # def remaining_capacity(self, package_weight):
    #     Actros.CAPACITY -= package_weight











