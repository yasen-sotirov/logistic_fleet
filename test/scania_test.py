from unittest import TestCase
from logistics_fleet.scania import Scania

VALID_TRUCK_ID = 1001
VALID_TRUCK_TYPE = "Scania"
VALID_ENROLL_TO_LOCATION = "SYDNEY"
VALID_CAPACITY = 42000
VALID_MAX_RANGE = 8000



class Scania_Should(TestCase):

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        # Arrange & Act
        scania = Scania(VALID_TRUCK_ID, VALID_TRUCK_TYPE, VALID_ENROLL_TO_LOCATION)

        # Assert
        self.assertEqual(VALID_TRUCK_ID, scania.UNIQUE_TRUCK_ID)
        self.assertEqual(VALID_CAPACITY, scania.CAPACITY)
        self.assertEqual(VALID_MAX_RANGE, scania.MAX_RANGE)

