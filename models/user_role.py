class UserRole:
    MANAGER = 'Manager'
    EMPLOYEE = 'Employee'
    SUPERVISOR = 'Supervisor'

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.MANAGER, cls.EMPLOYEE, cls.SUPERVISOR]:
            raise ValueError(f"None of the possible UserRole values matches the value {value}.")

        return value
