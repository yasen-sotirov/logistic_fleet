from core.application_data import ApplicationData
from commands.base_commands.base_command import BaseCommand
from core.validation_params import validate_location, validation_param_count, ValidationParamError
from errors.invalid_location_error import InvalidLocationError
from models.user import User


class SearchRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self.params, 1)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command CreateDeliveryPackage. Expected: 1, received: {len(self.params)}.'
        start_location = self._params[0]
        
        try:
            validate_location(start_location)
        except:
            InvalidLocationError
            return f'The following location is not supported: {start_location}.'
        if start_location.upper() == 'ALICE_SPRINGS':
            start_location = 'Alice Springs'
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'
        output = []
        spacer = '\n'
        for username in self._app_data._users:
            authorized = ['Supervisor', 'Manager']
            for user, user_credentials in User.all_users.items():
                if user == username:
                    for role in user_credentials:
                        if role == authorized[0] or role == authorized[1]:
                            accepted = True

        if not accepted:
            return 'You are not authorized to perform this operation.'   
        
        if len(self._app_data._all_delivery_routes) == 0:
            return f'There are no routes at location {start_location}'
        for route in self._app_data._all_delivery_routes:
            if route.start_location.upper() == start_location.upper():
                output.append(route)
        result = []
        for route_at_location in output:
            result.append(f'-----Route ID: {route_at_location.route_id}-----\n  Departure Location: {route_at_location.start_location}\n  Delivery location: {route_at_location.end_location}\n  Departure time: {route_at_location.date} {route_at_location.time}\n  Expected arrival time: {route_at_location.expected_arrival_time}')
        
        if result:
            return spacer.join(route_info for route_info in result)   
                     
        return 'You are not authorized to perform this operation.'
            