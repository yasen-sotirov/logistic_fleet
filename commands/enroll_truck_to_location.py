from commands.base_commands.base_command import BaseCommand
from errors.truck_errors import TruckIdError, TruckTypeError
from core.validation_params import ValidationParamError, validation_param_count, validate_location, validate_truck_type
from errors.invalid_location_error import InvalidLocationError
from logistics_fleet.actros import Actros
from logistics_fleet.man import Man
from logistics_fleet.scania import Scania


class EnrollTruckToLocation(BaseCommand):


    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)


    def execute(self):
        try:
            validation_param_count(self.params, 2)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command EnrollTruckToLocation. Expected: 2, received: {len(self.params)}.'

        truck_type, enrolled_to_location = self.params
        truck_type = truck_type.upper()
        enrolled_to_location = enrolled_to_location.upper()

        try:
            validate_truck_type(truck_type)
        except:
            TruckTypeError
            return f"The following truck type is not supported: {truck_type}."

        try:
            validate_location(enrolled_to_location)
        except:
            InvalidLocationError
            return f"The following location is not supported: {enrolled_to_location}."



        if truck_type.upper() == "ACTORS":
            try:
                if Actros.UNIQUE_TRUCK_ID not in Actros.TRUCK_ID_RANGE:
                    raise TruckIdError
                truck_id = Actros.UNIQUE_TRUCK_ID
                new_truck = Actros(truck_id, truck_type, enrolled_to_location)
                Actros.UNIQUE_TRUCK_ID += 1
            except:
                TruckIdError
                return f"There are no more available tucks from {truck_type.capitalize()} type."


        if truck_type.upper() == "MAN":
            try:
                if Man.UNIQUE_TRUCK_ID not in Man.TRUCK_ID_RANGE:
                    raise TruckIdError
                truck_id = Man.UNIQUE_TRUCK_ID
                new_truck = Man(truck_id, truck_type, enrolled_to_location)
                Man.UNIQUE_TRUCK_ID += 1
            except:
                TruckIdError
                return f"There are no more available tucks from {truck_type.capitalize()} type."


        if truck_type.upper() == "SCANIA":
            try:
                if Scania.UNIQUE_TRUCK_ID not in Scania.TRUCK_ID_RANGE:
                    raise TruckIdError
                truck_id = Scania.UNIQUE_TRUCK_ID
                new_truck = Scania(truck_id, truck_type, enrolled_to_location)
                Scania.UNIQUE_TRUCK_ID += 1
            except:
                TruckIdError
                return f"There are no more available tucks from {truck_type.capitalize()} type."


        output = self._app_data.add_truck_to_system(new_truck)
        return output





















