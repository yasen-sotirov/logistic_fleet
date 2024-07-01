from errors.validation_param_error import ValidationParamError
from map_distances.locations import Locations
from errors.invalid_location_error import InvalidLocationError
from logistics_fleet.truck import TruckTypes
from errors.truck_errors import TruckTypeError


def validation_param_count(params, count):
    if len(params) != count:
        raise ValidationParamError(f'Invalid number of arguments. Expected: {count}, recieved: {len(params)}.')


def try_parse_int(value):
    try:
        return int(value)
    except:
        raise ValueError("Invalid value. Should be an integer!")


def validate_location(value):
    try:
        _ = Locations(value.upper())
    except:
        raise InvalidLocationError("This location is not supported")


def validate_truck_type(value):
    try:
        _ = TruckTypes(value.upper())
    except:
        raise TruckTypeError("This truck type is not supported")