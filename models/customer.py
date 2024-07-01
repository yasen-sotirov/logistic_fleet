from models.package import Package
from errors.package_does_not_exist import PackageDoesNotExist

class Customer:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self._packages: list[Package] = []

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @property
    def packages(self):
        return tuple(self._packages)

    def add_package_to_customer(self, package: Package):
        for a_package in self._packages:
            if a_package.package_id == package.package_id:
                return f'Package already created for customer {self.first_name} {self.last_name}'
            
        self._packages.append(package)

    def find_customer_package(self, package_id: int):
        for a_package in self._packages:
            if a_package.package_id == package_id:
                return a_package
        
        return False
          
    def __str__(self):
        if len(self._packages) == 1:
            return f'Customer: {self.first_name} {self.last_name}, email: {self.email}, phone number: {self.phone_number} [1 package]'
        
        return f'Customer: {self.first_name} {self.last_name}, email: {self.email}, phone number: {self.phone_number} [{len(self._packages)} packages]'
