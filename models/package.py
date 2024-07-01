from map_distances.locations import Locations
from errors.invalid_location_error import InvalidLocationError


class Package:
    def __init__(
        self,
        package_id: int,
        start_location: str,
        end_location: str,
        weight,
        customer
    ):
        self._package_id = package_id
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self._customer = customer
        self._location_status = start_location.capitalize()
        self._assignation_status = 'Not assigned for dispatch'

    @property
    def package_id(self):
        return self._package_id

    @property
    def start_location(self):
        return self._start_location

    @property
    def end_location(self):
        return self._end_location

    @property
    def weight(self):
        return self._weight
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def assignation_status(self):
        return self._assignation_status
    
    @property
    def location_status(self):
        return self._location_status
    
    @assignation_status.setter
    def assignation_status(self, value: str):
        self._assignation_status = value


    
