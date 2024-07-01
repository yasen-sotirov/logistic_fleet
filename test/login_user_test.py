import unittest
from commands.login_user import LoginUser
from core.application_data import ApplicationData
from models.user import User
from core.validation_params import ValidationParamError


class LoginUser_Should(unittest.TestCase):
    def setUp(self):
        # Arrange, Act & Assert
        self.app_data = ApplicationData
        self.command = LoginUser([], self.app_data)

    def test_execute_successful_login(self, mock_input):
        pass

    def test_execute_failed_login(self, mock_input):
        pass

    def test_execute_validation_param_count_error(self, mock_input):
        pass
