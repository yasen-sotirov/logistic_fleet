from commands.base_commands.base_command import BaseCommand
from core.application_data import ApplicationData
from core.validation_params import validation_param_count, try_parse_int, ValidationParamError


class ViewCustomerByPhoneNumber(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
            
    def execute(self):
        try:
            validation_param_count(self.params, 2)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command ViewCustomerByPhoneNumber. Expected: 2, received: {len(self.params)}.'
        look_for_phone_number, look_for_package_id = self._params
        try:
            try_parse_int(look_for_package_id)
        except:
            ValueError
            return f'Invalid package id. It should be a number!'
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'
        find_customer = self._app_data.find_customer_by_phone_number(
            look_for_phone_number
        )
        if find_customer:
            find_package = find_customer.find_customer_package(int(look_for_package_id))
            if find_package == False:
                return f'Package with id {look_for_package_id} is not owned by customer: {find_customer.first_name} {find_customer.last_name}.'   
            if find_package.start_location.upper() != 'ALICE SPRINGS':
                find_package._start_location = find_package.start_location.capitalize()     
            if find_package.end_location.upper() != 'ALICE SPRINGS':
                find_package._end_location = find_package.end_location.capitalize()      
        else:
            return f"Customer with phone number {look_for_phone_number} does not exist!"
            
        spacer = "\n"
        return spacer.join(
            [
                f"Customer name: {find_customer.first_name} {find_customer.last_name}\n"
                f" # Phone number: {find_customer.phone_number}\n"
                f" # Email address: {find_customer.email}\n"
                f" # Number of packages for this customer: {len(find_customer._packages)}\n"
                f"   - Package ID: {find_package.package_id} [Starting location: {find_package._start_location} | End location: {find_package._end_location}]\n"
                f"   - Package current status: Package status: {find_package.assignation_status}"
            ]
        )

