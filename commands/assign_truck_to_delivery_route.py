from core.application_data import ApplicationData
from commands.base_commands.base_command import BaseCommand
from core.validation_params import validate_location, validation_param_count, try_parse_int, ValidationParamError
from errors.invalid_location_error import InvalidLocationError
from models.user import User


class AssignTruckToDeliveryRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self.params, 2)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command CreateDeliveryPackage. Expected: 2, received: {len(self.params)}.'
        start_location, delivery_route_id = self._params
        
        try:
            validate_location(start_location)
        except:
            InvalidLocationError
            return f'The following location is not supported: {start_location}.'
        try:
            try_parse_int(delivery_route_id)
        except:
            ValueError
            return f'Invalid route id. It should be a number!'
        
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'
        
        find_route = self._app_data.find_route_by_id(delivery_route_id)
        if find_route == False:
            return f'There is no route with ID: {delivery_route_id}'
        
        for username in self._app_data._users:
            authorized = ['Supervisor', 'Manager']
            for user, user_credentials in User.all_users.items():
                if user == username:
                    for role in user_credentials:
                        if role == authorized[0] or role == authorized[1]:
                            accepted = True

        if not accepted:
            return 'You are not authorized to perform this operation.'            

        find_truck = self._app_data.search_free_truck_by_location(start_location, find_route.total_distance_km)
        if find_truck:
            find_route.route_trucks.append(find_truck)
            find_truck.truck_status = f'Assigned to delivery route: {delivery_route_id}'
            return f'Truck {find_truck.truck_type}, ID: {find_truck._truck_id} has been assigned successfully to delivery route {delivery_route_id}.'
        elif find_truck == False:
            return f'there is no compatible truck at location: {start_location}'
                                

   
                        
            

