import unittest
from core.application_data import ApplicationData
from models.package import Package


class ApplicationData_should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()

    def test_add_package_to_system(self):
        package = Package(2, 'SYDNEY', 'MELBOURNE', 2, "Ivan Ivanov")
        result = self.app_data.add_package_to_system(package)

    def test_view_package(self):
        pass

    def test_add_truck_to_system(self):
        pass

    def test_view_trucks_at_location(self):
        pass

    def test_view_all_trucks(self):
        pass

    def test_view_unenroll_trucks(self):
        pass

    def test_login_user(self):
        pass

    def test_logout_user(self):
        pass

