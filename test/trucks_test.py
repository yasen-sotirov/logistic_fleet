from unittest import TestCase
from logistics_fleet.truck import Truck

VALID_TRUCK_ID = 1001
VALID_TRUCK_TYPE = "Actors"
VALID_ENROLL_TO_LOCATION = "SYDNEY"


class Trucks_Should(TestCase):
    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        # Arrange & Act
        truck = Truck(valid_truck_id, valid_truck_type, valid_enrolled_to_location)

        # Assert
        self.assertEqual(valid_truck_id, truck.truck_id)
        self.assertEqual(valid_truck_type, truck.truck_type)
        self.assertEqual(valid_enrolled_to_location, truck.enrolled_to_location)

