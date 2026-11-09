class User:
    """Representasi profil pengguna."""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")


class Admin(User):
    """Administrator, sebuah jenis user khusus."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("dewi", "kartika", "dewik", "dewi@example.com", "surakarta")
admin.show_privileges()