from core.validation_params import validation_param_count, validate_location, ValidationParamError, InvalidLocationError
from core.application_data import ApplicationData
from commands.base_commands.base_command import BaseCommand


class ViewPackages(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self.params, 1)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command ViewPackages. Expected: 1, received: {len(self.params)}.'
        location = self._params[0]
        try:
            validate_location(location)
        except:
            InvalidLocationError
            return f'The following location is not supported: {location}.'
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'
        output = self.app_data.view_packages(location)

        return output
        # return f'{(spacer.join([package for package in self._app_data._not_assigned_packages]))}'
