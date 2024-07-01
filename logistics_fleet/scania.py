from logistics_fleet.truck import Truck
from models.package import Package

class Scania(Truck):

    CAPACITY = 42000
    MAX_RANGE = 8000
    TRUCK_ID_RANGE = range(1001, 1010 + 1)
    UNIQUE_TRUCK_ID = 1001

    def __init__(self, truck_id: int, truck_type, enrolled_to_location):
        super().__init__(truck_id, truck_type, enrolled_to_location)
        self.capacity = Scania.CAPACITY

    @classmethod
    def unenroll_scania(cls):
        return Truck.unenroll_trucks(Scania.TRUCK_ID_RANGE, Scania.UNIQUE_TRUCK_ID)

    @property
    def remaining_capacity(self):
        return Scania.CAPACITY

    # def load_package_to_truck(self, package_to_load: Package):
        # if package_to_load.weight > Scania.remaining_capacity:
        #     return f"There is no enough space for package with ID {package_to_load.package_id}"
        # else:
        #     self.load.append(package_to_load)
        #     Scania.CAPACITY -= package_to_load.weight
        #     return f"Package with ID {package_to_load.package_id} has been loaded to truck with ID {self.truck_id}."