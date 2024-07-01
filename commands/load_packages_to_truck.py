from commands.base_commands.base_command import BaseCommand
from core.validation_params import ValidationParamError, try_parse_int, validation_param_count, validate_location, InvalidLocationError


class LoadPackagesToTruck(BaseCommand):
    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)


    def execute(self):
        try:
            validation_param_count(self.params, 2)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command LoadPackagesToTruck. Expected: 2, received: {len(self.params)}.'

        truck_for_load_id, route_id = self._params

        try:
            try_parse_int(truck_for_load_id)
        except:
            ValueError
            return f'Invalid truck ID. It should be a number!'
        
        try:
            try_parse_int(route_id)
        except:
            ValueError
            return f'Invalid route ID. It should be a number!'

        find_route = self._app_data.find_route_by_id(route_id)
        if find_route == False:
            return f'There is no route with ID: {route_id}'
        find_truck = self._app_data.find_truck_by_id(truck_for_load_id)
        if find_truck == False:
            return f'There is no truck with ID: {truck_for_load_id}'
    
        output = self._app_data.load_packages_to_truck(find_truck, find_route)

        return output





