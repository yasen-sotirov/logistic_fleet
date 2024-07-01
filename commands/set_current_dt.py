from core.application_data import ApplicationData
from commands.base_commands.base_command import BaseCommand
from core.date_time import DateTime, datetime


class SetCurrentDateTime(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        if len(self._params) == 0:
            DateTime.CURRENT_DATE_TIME = datetime.now().strftime('%d/%m/%Y %H:%M')

        else:
            if len(self._params) == 1 or len(self._params) > 2:
                return f'Invalid number of arguments for command SetCurrentDateTime. Expected Zero or 2, received: {len(self.params)}.'

            output = f"{self.params[0]} {self.params[1]}"

            time_check = DateTime.diff_between_dt(DateTime.CURRENT_DATE_TIME, output)
            if time_check <= 0:
                return f'Cannot set time in the past.'
            DateTime.CURRENT_DATE_TIME = output     

        for route in self._app_data._all_delivery_routes:
            if len(route.route_trucks) == 0:
                break
            check = DateTime.diff_between_dt(DateTime.CURRENT_DATE_TIME, route.expected_arrival_time)
            if check <= 0:
                route.delivery_status = 'Delivered'
                for truck in route._route_trucks:
                    if route.end_location.upper() == 'SYDNEY':
                        truck.truck_status = 'not assign to delivery route'
                        self._app_data._logistic_fleet_SYD.append(truck)
                        
                        for package in truck.load_space:
                            if package.end_location.upper() == route.end_location.upper():
                                package.assignation_status = 'Delivered'
                                self._app_data._not_assigned_packages_SYD.append(package)
                        truck.load_space.clear()

                    elif route.end_location.upper() == 'MELBOURNE':
                        truck.truck_status = 'not assign to delivery route'
                        self._app_data._logistic_fleet_MEL.append(truck)

                        for package in truck.load_space:
                            if package.end_location.upper() == route.end_location.upper():
                                package.assignation_status = 'Delivered'
                                self._app_data._not_assigned_packages_MEL.append(package)
                        truck.load_space.clear()

                    elif route.end_location.upper() == 'ADELAIDE':
                        truck.truck_status = 'not assign to delivery route'
                        self._app_data._logistic_fleet_ADL.append(truck)

                        for package in truck.load_space:
                            if package.end_location.upper() == route.end_location.upper():
                                package.assignation_status = 'Delivered'
                                self._app_data._not_assigned_packages_ADL.append(package)
                        truck.load_space.clear()

                    elif route.end_location.upper() == 'ALICE SPRINGS':
                        truck.truck_status = 'not assign to delivery route'
                        self._app_data._logistic_fleet_ASP.append(truck)

                        for package in truck.load_space:
                            if package.end_location.upper() == route.end_location.upper():
                                package.assignation_status = 'Delivered'
                                self._app_data._not_assigned_packages_ASP.append(package)
                        truck.load_space.clear()

                    elif route.end_location.upper() == 'BRISBANE':
                        truck.truck_status = 'not assign to delivery route'
                        self._app_data._logistic_fleet_BRI.append(truck)

                        for package in truck.load_space:
                            if package.end_location.upper() == route.end_location.upper():
                                package.assignation_status = 'Delivered'
                                self._app_data._not_assigned_packages_BRI.append(package)
                        truck.load_space.clear()

                    elif route.end_location.upper() == 'DARWIN':
                        truck.truck_status = 'not assign to delivery route'
                        self._app_data._logistic_fleet_DAR.append(truck)

                        for package in truck.load_space:
                            if package.end_location.upper() == route.end_location.upper():
                                package.assignation_status = 'Delivered'
                                self._app_data._not_assigned_packages_DAR.append(package)
                        truck.load_space.clear()

                    elif route.end_location.upper() == 'PERTH':
                        truck.truck_status = 'not assign to delivery route'
                        self._app_data._logistic_fleet_PER.append(truck)

                        for package in truck.load_space:
                            if package.end_location.upper() == route.end_location.upper():
                                package.assignation_status = 'Delivered'
                                self._app_data._not_assigned_packages_PER.append(package)
                        truck.load_space.clear()

                route._route_trucks.clear()

            elif check > 0:
                new_check = DateTime.diff_between_dt(DateTime.CURRENT_DATE_TIME, f'{route.date} {route.time}')
                if new_check <= 0:
                    route.delivery_status = 'On road'
                    for truck in route._route_trucks:
                        for package in truck.load_space:
                            package.assignation_status = 'On road'


        if len(self._app_data._all_delivery_routes) == 0:
            pass

        return f"Current time set to: ----- {DateTime.CURRENT_DATE_TIME} -----"
    

     # for package in route._route_trucks:
                    #     package.assignation_status = 'Delivered'
                   
                    