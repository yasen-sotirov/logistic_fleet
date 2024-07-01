from commands.base_commands.base_command import BaseCommand
from core.application_data import ApplicationData
from core.validation_params import validation_param_count, ValidationParamError
from models.user import User

class ViewRoutes(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self._params, 0)
        except:
            ValidationParamError
            return f"Invalid number of arguments for command ViewRoutes. Expected: 0, recieved: {len(self.params)}."
        
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'
        for username in self._app_data._users:
            authorized = ['Supervisor', 'Manager']
            for user, user_credentials in User.all_users.items():
                if user == username:
                    for role in user_credentials:
                        if role == authorized[0] or role == authorized[1]:
                            accepted = True

        if not accepted:
            return 'You are not authorized to perform this operation.'  
        
        spacer = '\n'
        output = []
        if len(self._app_data._all_delivery_routes) == 0:
            return f"There are no routes in the system."
        for route in self._app_data._all_delivery_routes:
            output.append(f'--Route ID: {route.route_id}--\n  Departure location: {route.start_location}\n  Delivery location: {route.end_location}\n  Total route distance in km: {route.total_distance_km}\n  Departure time: {route.date} {route.time}\n  Expected arrival time: {route.expected_arrival_time}\n  Delivery status: {route.delivery_status}\n  Trucks on this route: {len(route._route_trucks)}')

        return spacer.join(route_info for route_info in output)
        