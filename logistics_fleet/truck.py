from enum import Enum
from models.package import Package


class Truck:

    def __init__(self, truck_id: int, truck_type, enrolled_to_location):
        self._truck_id = truck_id
        self._truck_type = truck_type
        self.enrolled_to_location = enrolled_to_location
        self.capacity = None
        self._truck_status = "not assign to delivery route"
        self.load_space: list[Package] = []
        self.avg_speed = 84

    @property
    def truck_id(self):
        return self._truck_id

    @property
    def truck_type(self):
        return self._truck_type

    @staticmethod
    def unenroll_trucks(range_id, reached_id):
        range_end = range_id[len(range_id) - 1]
        return range_end - reached_id

    @property
    def truck_status(self):
        return self._truck_status

    @truck_status.setter
    def truck_status(self, value):
        self._truck_status = value
    






class TruckTypes(Enum):
    ACTORS = "ACTORS"
    MAN = "MAN"
    SCANIA = "SCANIA"


