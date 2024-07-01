from models.user_role import UserRole


class User:

    all_users = {
        "User_1": ["Petar Ivanov", "12345", "Manager"],
        "User_2": ["Ivan Petrov", "6789", "Employee"],
        "User_3": ["Georgi Todorov", "123", "Supervisor"],
        "User_4": ["Steven Peterson", "123", "Manager"],
        "User_5": ["Alice Steward", "321", "Employee"],
        "User_6": ["Dan Peterson", "3654", "Supervisor"]
        
    }

    def __init__(self, username, password, user_role):
        super().__init__(self, user_role)
        self._username = username
        self._password = password
        self._user_role = user_role

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def user_role(self):
        return self._user_role
