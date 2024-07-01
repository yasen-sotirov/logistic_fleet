from core.validation_params import validation_param_count, ValidationParamError
from core.application_data import ApplicationData
from commands.base_commands.base_command import BaseCommand
from core.date_time import DateTime


class CheckCurrentDateTime(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self.params, 0)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command CheckCurrentDateTime. Expected: 0, received: {len(self.params)}.'

        output = DateTime.CURRENT_DATE_TIME

        return f"Current date time is: {output}"
