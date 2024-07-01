from core.application_data import ApplicationData
from core.validation_params import validation_param_count, ValidationParamError
from models.user import User

class ViewAllCustomers:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        try:
            validation_param_count(self._params, 0)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command ViewAllCustomers. Expected: 0, received: {len(self._params)}.'
        
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'

        spacer = "\n"
        if len(self._app_data._customers) == 0:
            return f'There are no customers in the system.'
        
        return spacer.join([str(customer) for customer in  self._app_data._customers])

      