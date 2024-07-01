from core.validation_params import validation_param_count, ValidationParamError
from core.application_data import ApplicationData
from commands.base_commands.base_command import BaseCommand
from core.date_time import DateTime


class AddDaysToNow(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self.params, 1)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command SetCurrentDateTime. Expected: 1, received: {len(self.params)}.'

        days_as_str = int(self.params[0])
        DateTime.add_days_to_now(days_as_str)
        return f"Added {days_as_str} days. The date and the time is: {DateTime.CURRENT_DATE_TIME}"