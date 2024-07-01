from commands.base_commands.base_command import BaseCommand
from core.application_data import ApplicationData
from core.validation_params import validation_param_count, validate_location, ValidationParamError, InvalidLocationError
from models.delivery_route import DeliveryRoute
from core.date_time import DateTime, datetime, timedelta
from map_distances.distances_between_towns import calculate_distance
import math
from models.user import User

class CreateDeliveryRoute(BaseCommand):
    _unique_delivery_route_id = 3001

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self._params, 4)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command CreateDeliveryRoute. Expected: 4, received: {len(self.params)}.'
        start_date, starting_time, start_location, end_location = self._params
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
        
        time_check = DateTime.diff_between_dt(DateTime.CURRENT_DATE_TIME, f'{start_date} {starting_time}')
        if time_check <= 0:
            return f'Cannot create a delivery route starting in the past.'
        
        try:
            validate_location(start_location)
        except:
            InvalidLocationError
            return f'The following location is not supported: {start_location}.'
        try:
            validate_location(end_location)
        except:
            InvalidLocationError
            return f'The following location is not supported: {end_location}.'
        route_id = self._unique_delivery_route_id
        if start_location.lower() == 'alice_springs':
            start_location = 'Alice Springs'
            end_location = end_location.capitalize()
        elif end_location.lower() == 'alice_springs':
            start_location = start_location.capitalize()
            end_location = 'Alice Springs'
        else:
            start_location = start_location.capitalize()
            end_location = end_location.capitalize()

        route_distance = calculate_distance(start_location, end_location)
        route_hrs = (math.ceil(route_distance / 87 * 1.25))
        delivery_start_date = datetime.strptime(f'{start_date} {starting_time}', '%d/%m/%Y %H:%M')
        arrival_time = (delivery_start_date + timedelta(hours=route_hrs)).strftime("%d/%m/%Y %H:%M")

            

        new_route = DeliveryRoute(route_id, start_date, starting_time, start_location, end_location, route_distance, route_hrs, arrival_time)
        output = self._app_data.add_route_to_system(new_route)
        

        CreateDeliveryRoute._unique_delivery_route_id += 1

        return output
            
    





        # asd = str(datetime.fromtimestamp(time_check).strftime("%d/%m/%Y %H:%M"))
        # dfg = DateTime.add_time_to_date(f'{start_date} {starting_time}', asd)
        # arrival_time = datetime.fromtimestamp(dfg).strftime("%d/%m/%Y %H:%M")
        # myday = datetime.strptime(DateTime.CURRENT_DATE_TIME, '%Y-%m-%d')
        # arrival_time = datetime.strptime(asd, '%d/%m/%Y %H:%M')
