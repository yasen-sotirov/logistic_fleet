from commands.base_commands.base_command import BaseCommand
from core.validation_params import validation_param_count, ValidationParamError
from models.user import User
from core.application_data import ApplicationData


class LoginUser(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            validation_param_count(self._params, 0)
        except:
            ValidationParamError
            return f'Invalid number of arguments for command login_user. Expected: 0, received: {len(self.params)}.'

        for k, v in User.all_users.items():
            if k == username:
                if v[1] == password:
                    self._app_data.login_user(username)

                    return f"User {username} successfully logged in!"

        return "Wrong username or password!"
