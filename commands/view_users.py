from commands.base_commands.base_command import BaseCommand
from core.application_data import ApplicationData
from core.validation_params import validation_param_count, ValidationParamError


class ViewUsers(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self._params, 0)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command ViewUsers. Expected: 0, received: {len(self._params)}.'
        spacer = "\n"

        return spacer.join([str(user) for user in self._app_data._users])

