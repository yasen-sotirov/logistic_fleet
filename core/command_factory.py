from core.application_data import ApplicationData
from commands.create_delivery_package import CreateDeliveryPackage
from commands.crate_delivery_route import CreateDeliveryRoute
from commands.search_route import SearchRoute
from commands.assign_truck_to_delivery_route import AssignTruckToDeliveryRoute
from commands.load_packages_to_truck import LoadPackagesToTruck
from commands.view_packages import ViewPackages
from commands.view_routes import ViewRoutes
from commands.view_trucks_at_location import ViewTrucksAtLocation
from commands.view_all_customers import ViewAllCustomers
from commands.view_customer_by_phone_number import ViewCustomerByPhoneNumber
from commands.set_current_dt import SetCurrentDateTime
from commands.check_current_dt import CheckCurrentDateTime
from commands.login_user import LoginUser
from commands.logout_user import LogoutUser
from commands.add_days_to_now import AddDaysToNow
from commands.view_unassigned_packages import ViewUnassignedPackages
from commands.enroll_truck_to_location import EnrollTruckToLocation
from commands.view_users import ViewUsers
from commands.view_all_trucks import ViewAllTrucks
from commands.view_unenroll_trucks import ViewUnenrollTrucks


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line: str):
        cmd, *params = input_line.split()

        if cmd.lower() == "createdeliverypackage":
            return CreateDeliveryPackage(params, self._app_data)
        elif cmd.lower() == "createdeliveryroute":
            return CreateDeliveryRoute(params, self._app_data)
        elif cmd.lower() == "searchroute":
            return SearchRoute(params, self._app_data)
        elif cmd.lower() == "assigntrucktodeliveryroute":
            return AssignTruckToDeliveryRoute(params, self._app_data)
        elif cmd.lower() == "loadpackagestotruck":
            return LoadPackagesToTruck(params, self._app_data)
        elif cmd.lower() == "viewroutes":
            return ViewRoutes(params, self._app_data)
        elif cmd.lower() == "viewpackages":
            return ViewPackages(params, self._app_data)
        elif cmd.lower() == "viewtrucksatlocation":
            return ViewTrucksAtLocation(params, self._app_data)
        elif cmd.lower() == "viewcustomerbyphonenumber":
            return ViewCustomerByPhoneNumber(params, self._app_data)
        elif cmd.lower() == "viewallcustomers":
            return ViewAllCustomers(params, self._app_data)
        elif cmd.lower() == "viewunassignedpackages":
            return ViewUnassignedPackages(params, self._app_data)
        elif cmd.lower() == "setcurrentdatetime":
            return SetCurrentDateTime(params, self._app_data)
        elif cmd.lower() == "checkcurrentdatetime":
            return CheckCurrentDateTime(params, self._app_data)
        elif cmd.lower() == "login":
            return LoginUser(params, self._app_data)
        elif cmd.lower() == "logout":
            return LogoutUser(params, self._app_data)
        elif cmd.lower() == "adddaystonow":
            return AddDaysToNow(params, self._app_data)
        elif cmd.lower() == "viewunassignedpackages":
            return ViewUnassignedPackages(params, self._app_data) 
        elif cmd.lower() == "enrolltrucktolocation":
            return EnrollTruckToLocation(params, self._app_data)
        elif cmd.lower() == "viewusers":
            return ViewUsers(params, self._app_data)
        elif cmd.lower() == "viewalltrucks":
            return ViewAllTrucks(params, self._app_data)
        elif cmd.lower() == "viewusers":
            return ViewUsers(params, self._app_data)
        elif cmd.lower() == "viewunenrolltrucks":
            return ViewUnenrollTrucks(params, self._app_data)

        else:
            return f"The following command not supported: {cmd}! Please type a correct command!"
