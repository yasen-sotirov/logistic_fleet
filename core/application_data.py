from models.package import Package
from errors.invalid_location_error import InvalidLocationError
from map_distances.locations import Locations
from models.customer import Customer
from models.delivery_route import DeliveryRoute
from map_distances.distances_between_towns import distances
from models.user import User
from logistics_fleet.scania import Scania, Truck
from logistics_fleet.man import Man
from logistics_fleet.actros import Actros


class ApplicationData:
    def __init__(self):
        self._not_assigned_packages_SYD: list[Package] = []
        self._not_assigned_packages_MEL: list[Package] = []
        self._not_assigned_packages_ADL: list[Package] = []
        self._not_assigned_packages_ASP: list[Package] = []
        self._not_assigned_packages_BRI: list[Package] = []
        self._not_assigned_packages_DAR: list[Package] = []
        self._not_assigned_packages_PER: list[Package] = []

        self._all_packages: list[Package] = []
        self._customers: list[Customer] = []

        self._all_delivery_routes: list[DeliveryRoute] = []
        
        self._logistic_fleet_SYD: list[Truck] = []
        self._logistic_fleet_MEL = []
        self._logistic_fleet_ADL = []
        self._logistic_fleet_ASP = []
        self._logistic_fleet_BRI = []
        self._logistic_fleet_DAR = []
        self._logistic_fleet_PER = []
        self._all_trucks: list[Truck] = []

        self._users: list[User] = []



    def _find_customer(
        self, first_name: str, last_name: str, email: str, phone_number: str
    ):
        for customer in self._customers:
            if customer.phone_number == phone_number:
                return customer

        new_customer = Customer(first_name, last_name, email, phone_number)
        self._customers.append(new_customer)

        return new_customer

    def find_customer_by_phone_number(self, look_for_phone_number: str):
        for customer in self._customers:
            if customer.phone_number == look_for_phone_number:
                return customer

        return False
    
    def find_route_by_id(self, looking_for_route_id: str):
        for route in self._all_delivery_routes:
            if int(route.route_id) == int(looking_for_route_id):
                return route

        return False
    
    def find_truck_by_id(self, looking_for_truck_id: str):
        for truck in self._all_trucks:
            if int(truck.truck_id) == int(looking_for_truck_id):
                return truck

        return False

    def add_route_to_system(self, new_route: DeliveryRoute):
        self._all_delivery_routes.append(new_route)

        return f"Route with ID: {new_route._route_id} has been created. Starting location: {new_route.start_location}"

    def add_package_to_system(self, package: Package):
        if package.start_location.upper() == "SYDNEY":
            self._not_assigned_packages_SYD.append(package)
            package._assignation_status = 'not assigned'
            self._all_packages.append(package)
        elif package.start_location.upper() == "MELBOURNE":
            self._not_assigned_packages_MEL.append(package)
            package._assignation_status = 'not assigned'
            self._all_packages.append(package)
        elif package.start_location.upper() == "ADELAIDE":
            self._not_assigned_packages_ADL.append(package)
            package._assignation_status = 'not assigned'
            self._all_packages.append(package)
        elif package.start_location.upper() == "ALICE SPRINGS":
            self._not_assigned_packages_ASP.append(package)
            package._assignation_status = 'not assigned'
            self._all_packages.append(package)
            return f"New package has been created successfully. ID of the package is: {package.package_id}. The package is located in Alice Springs department"
        elif package.start_location.upper() == "BRISBANE":
            self._not_assigned_packages_BRI.append(package)
            package._assignation_status = 'not assigned'
            self._all_packages.append(package)
        elif package.start_location.upper() == "DARWIN":
            self._not_assigned_packages_DAR.append(package)
            package._assignation_status = 'not assigned'
            self._all_packages.append(package)
        elif package.start_location.upper() == "PERTH":
            self._not_assigned_packages_PER.append(package)
            package._assignation_status = 'not assigned'
            self._all_packages.append(package)

        return f"New package has been created successfully. ID of the package is: {package.package_id}. The package is located in {package.start_location.capitalize()} department"

    def view_packages(self, location: str):
        try:
            _ = Locations(location.upper())
        except ValueError:
            raise InvalidLocationError(
                f"The following location is not supported: {location}"
            )
        if location.upper() == "SYDNEY":
            spacer = "\n"
            if len(self._not_assigned_packages_SYD) == 0:
                return f"There are no packages in {location.capitalize()} department!"
            else:
                return spacer.join(
                    [
                        f"Department: [{location.capitalize()}]\n"
                        f" -Total ammount of packages: {len(self._not_assigned_packages_SYD)}"
                    ]
                )

        elif location.upper() == "MELBOURNE":
            spacer = "\n"
            if len(self._not_assigned_packages_MEL) == 0:
                return f"There are no packages in {location.capitalize()} department!"
            else:
                return spacer.join(
                    [
                        f"Department: [{location.capitalize()}]\n"
                        f" -Total ammount of packages: {len(self._not_assigned_packages_MEL)}"
                    ]
                )

        elif location.upper() == "ADELAIDE":
            spacer = "\n"
            if len(self._not_assigned_packages_ADL) == 0:
                return f"There are no packages in {location.capitalize()} department!"
            else:
                return spacer.join(
                    [
                        f"Department: [{location.capitalize()}]\n"
                        f" -Total ammount of packages: {len(self._not_assigned_packages_ADL)}"
                    ]
                )

        elif location.upper() == "ALICE_SPRINGS":
            spacer = "\n"
            if len(self._not_assigned_packages_ASP) == 0:
                return f"There are no packages in Alice Springs department!"
            else:
                return spacer.join(
                    [
                        f"Department: [Alice Springs]\n"
                        f" -Total ammount of packages: {len(self._not_assigned_packages_ASP)}"
                    ]
                )

        elif location.upper() == "BRISBANE":
            spacer = "\n"
            if len(self._not_assigned_packages_BRI) == 0:
                return f"There are no packages in {location.capitalize()} department!"
            else:
                return spacer.join(
                    [
                        f"Department: [{location.capitalize()}]\n"
                        f" -Total ammount of packages: {len(self._not_assigned_packages_BRI)}"
                    ]
                )

        elif location.upper() == "DARWIN":
            spacer = "\n"
            if len(self._not_assigned_packages_DAR) == 0:
                return f"There are no packages in {location.capitalize()} department!"
            else:
                return spacer.join(
                    [
                        f"Department: [{location.capitalize()}]\n"
                        f" -Total ammount of packages: {len(self._not_assigned_packages_DAR)}"
                    ]
                )
        elif location.upper() == "PERTH":
            spacer = "\n"
            if len(self._not_assigned_packages_PER) == 0:
                return f"There are no packages in {location.capitalize()} department!"
            else:
                return spacer.join(
                    [
                        f"Department: [{location.capitalize()}]\n"
                        f" -Total ammount of packages: {len(self._not_assigned_packages_PER)}"
                    ]
                )


    def add_truck_to_system(self, truck):
        if truck.enrolled_to_location== "SYDNEY":
            self._logistic_fleet_SYD.append(truck)
            self._all_trucks.append(truck)

        elif truck.enrolled_to_location == "MELBOURNE":
            self._logistic_fleet_MEL.append(truck)
            self._all_trucks.append(truck)

        elif truck.enrolled_to_location == "ADELAIDE":
            self._logistic_fleet_ADL.append(truck)
            self._all_trucks.append(truck)

        elif truck.enrolled_to_location == "ALICE_SPRINGS":
            truck.enrolled_to_location == 'Alice Springs'
            self._logistic_fleet_ASP.append(truck)
            self._all_trucks.append(truck)

        elif truck.enrolled_to_location == "BRISBANE":
            self._logistic_fleet_BRI.append(truck)
            self._all_trucks.append(truck)

        elif truck.enrolled_to_location == "DARWIN":
            self._logistic_fleet_DAR.append(truck)
            self._all_trucks.append(truck)

        elif truck.enrolled_to_location == "PERTH":
            self._logistic_fleet_PER.append(truck)
            self._all_trucks.append(truck)

        if truck.enrolled_to_location == 'ALICE_SPRINGS':
            return (f"New truck type {truck.truck_type}, with ID {truck.truck_id} has been added to "
                f"Alice Springs logistic fleet.")

        return (f"New truck type {truck.truck_type}, with ID {truck.truck_id} has been added to "
                f"{truck.enrolled_to_location.capitalize()} logistic fleet.")


    def view_trucks_at_location(self, location: str):

        if location.upper() == "SYDNEY":
            spacer = "\n"
            if len(self._logistic_fleet_SYD) == 0:
                return f"There are no assigned trucks in {location.capitalize()}."
            else:
                truck_list = []
                for truck in self._logistic_fleet_SYD:
                    truck_list.append(f"    Truck ID: {truck.truck_id}, "
                                      f"truck type: {truck.truck_type}, "
                                      f"truck status: {truck.truck_status}")

                all_trucks = spacer.join([f"Department {location.capitalize()}."
                        f" Total amount of trucks: {len(self._logistic_fleet_SYD)}"])
                trucks_by_type = spacer.join(truck_list)
                return all_trucks + spacer + trucks_by_type + spacer


        if location.upper() == "MELBOURNE":
            spacer = "\n"
            if len(self._logistic_fleet_MEL) == 0:
                return f"There are no trucks in {location.capitalize()}."
            else:
                truck_list = []
                for truck in self._logistic_fleet_MEL:
                    truck_list.append(f"    Truck ID: {truck.truck_id}, "
                                      f"truck type: {truck.truck_type}, "
                                      f"truck status: {truck.truck_status}")

                all_trucks = spacer.join([f"Department {location.capitalize()}."
                                          f" Total amount of trucks: {len(self._logistic_fleet_MEL)}"])
                trucks_by_type = spacer.join(truck_list)
                return all_trucks + spacer + trucks_by_type + spacer


        if location.upper() == "ADELAIDE":
            spacer = "\n"
            if len(self._logistic_fleet_ADL) == 0:
                return f"There are no trucks in {location.capitalize()}."
            else:
                truck_list = []
                for truck in self._logistic_fleet_ADL:
                    truck_list.append(f"    Truck ID: {truck.truck_id}, "
                                      f"truck type: {truck.truck_type}, "
                                      f"truck status: {truck.truck_status}")

                all_trucks = spacer.join([f"Department {location.capitalize()}."
                                          f" Total amount of trucks: {len(self._logistic_fleet_ADL)}"])
                trucks_by_type = spacer.join(truck_list)
                return all_trucks + spacer + trucks_by_type + spacer


        if location.upper() == "ALICE_SPRINGS":
            spacer = "\n"
            if len(self._logistic_fleet_ASP) == 0:
                return f'There are no trucks in Alice Springs'
            else:
                truck_list = []
                for truck in self._logistic_fleet_ASP:
                    truck_list.append(f"    Truck ID: {truck.truck_id}, "
                                      f"truck type: {truck.truck_type}, "
                                      f"truck status: {truck.truck_status}")

                all_trucks = spacer.join([f"Department Alice Springs."
                                          f" Total amount of trucks: {len(self._logistic_fleet_ASP)}"])
                trucks_by_type = spacer.join(truck_list)
                return all_trucks + spacer + trucks_by_type + spacer


        if location.upper() == "BRISBANE":
            spacer = "\n"
            if len(self._logistic_fleet_BRI) == 0:
                return f"There are no trucks in {location.capitalize()}."
            else:
                truck_list = []
                for truck in self._logistic_fleet_BRI:
                    truck_list.append(f"    Truck ID: {truck.truck_id}, "
                                      f"truck type: {truck.truck_type}, "
                                      f"truck status: {truck.truck_status}")

                all_trucks = spacer.join([f"Department {location.capitalize()}."
                                          f" Total amount of trucks: {len(self._logistic_fleet_BRI)}"])
                trucks_by_type = spacer.join(truck_list)
                return all_trucks + spacer + trucks_by_type + spacer


        if location.upper() == "DARWIN":
            spacer = "\n"
            if len(self._logistic_fleet_DAR) == 0:
                return f"There are no trucks in {location.capitalize()}."
            else:
                truck_list = []
                for truck in self._logistic_fleet_DAR:
                    truck_list.append(f"    Truck ID: {truck.truck_id}, "
                                      f"truck type: {truck.truck_type}, "
                                      f"truck status: {truck.truck_status}")

                all_trucks = spacer.join([f"Department {location.capitalize()}."
                                          f" Total amount of trucks: {len(self._logistic_fleet_DAR)}"])
                trucks_by_type = spacer.join(truck_list)
                return all_trucks + spacer + trucks_by_type + spacer


        if location.upper() == "PERTH":
            spacer = "\n"
            if len(self._logistic_fleet_PER) == 0:
                return f"There are no trucks in {location.capitalize()}."
            else:
                truck_list = []
                for truck in self._logistic_fleet_PER:
                    truck_list.append(f"    Truck ID: {truck.truck_id}, "
                                      f"truck type: {truck.truck_type}, "
                                      f"truck status: {truck.truck_status}")

                all_trucks = spacer.join([f"Department {location.capitalize()}."
                                          f"Total amount of trucks: {len(self._logistic_fleet_PER)}"])
                trucks_by_type = spacer.join(truck_list)
                return all_trucks + spacer + trucks_by_type + spacer


    def view_all_trucks(self):
        if len(self._all_trucks) == 0:
            return f"There are no enroll trucks at any department."
        else:
            return (f"Total amount of trucks in all departments {len(self._all_trucks)}\n"
                    f"  Total amount of trucks on department Sydney: {len(self._logistic_fleet_SYD)}\n"
                    f"  Total amount of trucks on department Melbourne: {len(self._logistic_fleet_MEL)}\n"
                    f"  Total amount of trucks on department Adelaide: {len(self._logistic_fleet_ADL)}\n"
                    f"  Total amount of trucks on department Alice Springs: {len(self._logistic_fleet_ASP)}\n"
                    f"  Total amount of trucks on department Brisbane: {len(self._logistic_fleet_BRI)}\n"
                    f"  Total amount of trucks on department Darwin: {len(self._logistic_fleet_DAR)}\n"
                    f"  Total amount of trucks on department Perth: {len(self._logistic_fleet_PER)}\n")


    def view_unenroll_trucks(self):
        all_possible_trucks = 40
        if len(self._all_trucks) == all_possible_trucks:
            return f"There are no unenroll trucks."
        else:
            unenroll_actors = Actros.unenroll_actors()
            unenroll_man = Man.unenroll_man()
            unenroll_scania = Scania.unenroll_scania()
            return (f"Not assigned truck:\n"
                    f" - Actors: {unenroll_actors}\n"
                    f" - Man: {unenroll_man}\n"
                    f" - Scania: {unenroll_scania}\n")


    def login_user(self, username):
        if username not in self._users:
            self._users.append(username)

    def logout_user(self, username):
        if username in self._users:
            self._users.remove(username)

    def view_log_users(self):
        all_users = self._users
        return all_users


    def load_packages_to_truck(self, truck_for_load: Truck, route_for_load: DeliveryRoute):
        founded_packages = []
        for package in self._all_packages:
            if package.start_location.upper() == route_for_load.start_location.upper() and package.end_location.upper() == route_for_load.end_location.upper():
                founded_packages.append(package)

        if len(founded_packages) == 0:
            return f'There are no packages that can be loaded.'
        
        while True:
            total_weight_loaded = 0
            counter = 0
            for package in founded_packages:
                total_weight_loaded += int(package.weight)
                if total_weight_loaded >= int(truck_for_load.CAPACITY):
                    total_weight_loaded -= int(package.weight)
                    break
                if package.start_location.upper() == 'SYDNEY':
                    self._not_assigned_packages_SYD.remove(package)
                elif package.start_location.upper() == 'MELBOURNE':
                    self._not_assigned_packages_MEL.remove(package)
                elif package.start_location.upper() == 'ADELAIDE':
                    self._not_assigned_packages_ADL.remove(package)
                elif package.start_location.upper() == 'ALICE SPRINGS':
                    self._not_assigned_packages_ASP.remove(package)
                elif package.start_location.upper() == 'BRISBANE':
                    self._not_assigned_packages_BRI.remove(package)
                elif package.start_location.upper() == 'DARWIN':
                    self._not_assigned_packages_DAR.remove(package)
                elif package.start_location.upper() == 'PERTH':
                    self._not_assigned_packages_PER.remove(package)
                
                package.assignation_status = 'Loaded'
                truck_for_load.load_space.append(package)
                counter += 1
            
            return (f"Truck type {truck_for_load.truck_type.capitalize()}, ID: {truck_for_load.truck_id} has been loaded with "
                    f"{counter} packages with total weight {total_weight_loaded} kg.\n"
                    f"  Free space left in truck: {truck_for_load.CAPACITY - total_weight_loaded} kg.\n"
                    f"  Number of packages left in the warehouse: {len(self._not_assigned_packages_SYD)}\n")

        # if location_warehouse_name.upper() == "PERTH":
        #     try:
        #         for current_truck in self._logistic_fleet_PER:
        #             if current_truck.truck_id == truck_for_load_id:
        #                 truck_for_load = current_truck
        #                 break
        #     except:
        #         TruckIdError
        #         return f"In this warehouse there is no tuck with ID {truck_for_load_id}."

        #     loaded_packages_weight = 0
        #     loaded_packages_number = 0
        #     missed_packages = []

        #     for el in range(len(self._not_assigned_packages_PER)):
        #         package_to_load = self._not_assigned_packages_PER[0]
        #         package_weight = int(package_to_load.weight)
        #         if package_weight > truck_for_load.CAPACITY:
        #             missed_packages.append(package_to_load.package_id)
        #         else:
        #             for route in self._all_delivery_routes:
        #                 if int(route.route_id) == int(route_for_load_id):
        #                     truck_for_load.CAPACITY -= package_weight
        #                     if route.end_location.upper() == package_to_load.end_location.upper():
        #                         truck_for_load.load_space.append(package_to_load)
        #                         self._not_assigned_packages_PER.remove(package_to_load)
        #                         package_to_load.assignation_status = "Loaded"
        #                         loaded_packages_weight += package_weight
        #                         loaded_packages_number += 1

        #     return (f"Truck type {truck_for_load.truck_type.capitalize()} has been loaded with "
        #             f"{loaded_packages_number} packages with total weight {loaded_packages_weight} kg.\n"
        #             f"  Free space left in truck: {truck_for_load.CAPACITY} kg.\n"
        #             f"  Number of packages left in the warehouse: {len(self._not_assigned_packages_PER)}\n")


    def search_free_truck_by_location(self, location, distance):
        if location.upper() == 'SYDNEY':
            for truck in self._logistic_fleet_SYD:
                if truck.MAX_RANGE >= int(distance) and truck._truck_status == 'not assign to delivery route':
                    self._logistic_fleet_SYD.remove(truck)
                    return truck
        elif location.upper() == 'MELBOURNE':
            for truck in self._logistic_fleet_MEL:
                if truck.MAX_RANGE >= int(distance):
                    self._logistic_fleet_MEL.remove(truck)
                    return truck
        elif location.upper() == 'ADELAIDE':
            for truck in self._logistic_fleet_ADL:
                if truck.MAX_RANGE >= int(distance):
                    self._logistic_fleet_ADL.remove(truck)
                    return truck 
        elif location.upper() == 'ALICE_SPRINGS':
            for truck in self._logistic_fleet_ASP:
                if truck.MAX_RANGE >= int(distance):
                    self._logistic_fleet_ASP.remove(truck)
                    return truck
        elif location.upper() == 'BRISBANE':
            for truck in self._logistic_fleet_BRI:
                if truck.MAX_RANGE >= int(distance):
                    self._logistic_fleet_BRI.remove(truck)
                    return truck
        elif location.upper() == 'DARWIN':
            for truck in self._logistic_fleet_DAR:
                if truck.MAX_RANGE >= int(distance):
                    self._logistic_fleet_DAR.remove(truck)
                    return truck
        elif location.upper() == 'PERTH':
            for truck in self._logistic_fleet_PER:
                if truck.MAX_RANGE >= int(distance):
                    self._logistic_fleet_PER.remove(truck)
                    return truck

        return False