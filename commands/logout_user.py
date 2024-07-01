from commands.base_commands.base_command import BaseCommand
from core.application_data import ApplicationData


class LogoutUser(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        username = input("Enter username: ")

        self._app_data.logout_user(username)

        return f"User {username} logged out successfully!"
