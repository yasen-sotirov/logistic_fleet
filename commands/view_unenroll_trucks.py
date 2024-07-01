from core.validation_params import validation_param_count, ValidationParamError
from core.application_data import ApplicationData
from commands.base_commands.base_command import BaseCommand


class ViewUnenrollTrucks(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self.params, 0)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command ViewUnenrollTrucks. Expected: 0, recieved: {len(self.params)}.'

        output = self.app_data.view_unenroll_trucks()

        return output

