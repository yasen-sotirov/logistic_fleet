from logistics_fleet.truck import Truck
from models.package import Package

class Man(Truck):

    CAPACITY = 37000
    MAX_RANGE = 10000
    TRUCK_ID_RANGE = range(1011, 1025 + 1)
    UNIQUE_TRUCK_ID = 1011

    def __init__(self, truck_id: int, truck_type, enrolled_to_location):
        super().__init__(truck_id, truck_type, enrolled_to_location)
        self.capacity = Man.CAPACITY

    @classmethod
    def unenroll_man(cls):
        return Truck.unenroll_trucks(Man.TRUCK_ID_RANGE, Man.UNIQUE_TRUCK_ID)

    @property
    def remaining_capacity(self):
        return Man.CAPACITY

    def load_package_to_truck(self, package_to_load: Package):
        if package_to_load.weight > Man.remaining_capacity:
            return f"There is no enough space for package with ID {package_to_load.package_id}"
        else:
            self.load.append(package_to_load)
            Man.CAPACITY -= package_to_load.weight
            return f"Package with ID {package_to_load.package_id} has been loaded to truck with ID {self.truck_id}."