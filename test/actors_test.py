from unittest import TestCase
from logistics_fleet.actros import Actros

VALID_TRUCK_ID = 1026
VALID_TRUCK_TYPE = "Actors"
VALID_ENROLL_TO_LOCATION = "SYDNEY"
VALID_CAPACITY = 26000
VALID_MAX_RANGE = 13000



class Actors_Should(TestCase):

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        # Arrange & Act
        actors = Actros(VALID_TRUCK_ID, VALID_TRUCK_TYPE, VALID_ENROLL_TO_LOCATION)

        # Assert
        self.assertEqual(VALID_TRUCK_ID, actors.UNIQUE_TRUCK_ID)
        self.assertEqual(VALID_CAPACITY, actors.CAPACITY)
        self.assertEqual(VALID_MAX_RANGE, actors.MAX_RANGE)
