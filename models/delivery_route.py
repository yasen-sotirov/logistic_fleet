from map_distances.locations import Locations
from logistics_fleet.truck import Truck


class DeliveryRoute:
    def __init__(self, route_id, date, time, start_location: str, end_location: str, total_distance_km, total_route_hours, expected_arrival_time: str):
        self._route_id = route_id
        self._date = date
        self._time = time
        self._start_location = start_location
        self._end_location = end_location
        self._total_distance_km = total_distance_km
        self._total_route_hours = total_route_hours
        self._expected_arrival_time = expected_arrival_time
        self.delivery_status = 'For dispatch'
        self._route_trucks = []
        
    @property
    def route_id(self):
        return self._route_id

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def start_location(self):
        return self._start_location

    @property
    def end_location(self):
        return self._end_location
    
    @property
    def total_distance_km(self):
        return self._total_distance_km
    
    @property
    def total_route_hours(self):
        return self._total_route_hours
    
    @property
    def expected_arrival_time(self):
        return self._expected_arrival_time
    
    @property
    def delivery_status(self):
        return self._delivery_status
    
    @delivery_status.setter
    def delivery_status(self, value: str):
        valid_status = ['For dispatch', 'On road', 'Delivered']
        if value in valid_status:
            self._delivery_status = value

    @property
    def route_trucks(self):
        return self._route_trucks
    
    @route_trucks.setter
    def route_trucks(self, value: Truck):
        self._route_trucks.append(value)
