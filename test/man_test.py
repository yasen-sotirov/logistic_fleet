from unittest import TestCase
from logistics_fleet.man import Man

VALID_TRUCK_ID = 1011
VALID_TRUCK_TYPE = "Man"
VALID_ENROLL_TO_LOCATION = "SYDNEY"
VALID_CAPACITY = 37000
VALID_MAX_RANGE = 10000



class Man_Should(TestCase):

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        # Arrange & Act
        man = Man(VALID_TRUCK_ID, VALID_TRUCK_TYPE, VALID_ENROLL_TO_LOCATION)

        # Assert
        self.assertEqual(VALID_TRUCK_ID, man.UNIQUE_TRUCK_ID)
        self.assertEqual(VALID_CAPACITY, man.CAPACITY)
        self.assertEqual(VALID_MAX_RANGE, man.MAX_RANGE)
