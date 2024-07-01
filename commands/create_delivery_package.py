from commands.base_commands.base_command import BaseCommand
from core.application_data import ApplicationData
from core.validation_params import validation_param_count, validate_location, ValidationParamError, InvalidLocationError

from models.package import Package


class CreateDeliveryPackage(BaseCommand):
    _unique_package_id = 2001

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self.params, 7)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command CreateDeliveryPackage. Expected: 7, received: {len(self.params)}.'
        start_location, end_location, weight, customer_first_name, customer_last_name, customer_email, customer_phone_number = self._params
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'
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
        new_customer = self.app_data._find_customer(customer_first_name, customer_last_name, customer_email, customer_phone_number)
        package_id = self._unique_package_id
        if start_location.upper() == 'ALICE_SPRINGS':
            start_location = 'Alice Springs'
        if end_location.upper() == 'ALICE_SPRINGS':
            end_location = 'Alice Springs'
        new_package = Package(package_id, start_location, end_location, weight, new_customer)
        output = self._app_data.add_package_to_system(new_package)
        _ = new_customer.add_package_to_customer(new_package)

        CreateDeliveryPackage._unique_package_id += 1

        # return output
        return f'{new_package.start_location}, {new_package.end_location}'
    
    

