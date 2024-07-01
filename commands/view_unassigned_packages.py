from commands.base_commands.base_command import BaseCommand
from core.application_data import ApplicationData
from core.validation_params import validation_param_count, ValidationParamError
from models.user import User



class ViewUnassignedPackages(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        try:
            validation_param_count(self._params, 0)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command ViewUnassignedPackages. Expected: 0, received: {len(self.params)}.'

        output = []
        if len(self._app_data._users) == 0:
            return f'Please log in to continue.'
        for username in self._app_data._users:
            authorized = 'Manager'
            for user, user_role in User.all_users.items():
                if user == username:
                    for role in user_role:
                        if role == authorized:
                            if len(self._app_data._all_packages) == 0:
                                return 'There are no packages in the system.'
                            for package in self._app_data._all_packages:
                                if package._assignation_status == 'not assigned':
                                    if package.location_status.upper() == 'ALICE_SPRINGS':
                                        output.append(f'Package ID: {package.package_id} - location: Alice Springs')

                                    output.append(f'Package ID: {package.package_id} - location: {package.location_status}')
                                
                            spacer = "\n"

                            return spacer.join([package_info for package_info in output])
                        
            return 'You are not authorized to perform this operation.'