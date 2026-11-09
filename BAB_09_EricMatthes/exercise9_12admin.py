from exercise9_12admin import User


class Privileges:
    """Classes yang merepresentasikan privileges dan admin."""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Administrator, sebuah jenis user khusus."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()