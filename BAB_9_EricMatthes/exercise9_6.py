class Restaurant:
    """Representasi sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    """Kios es krim, sebuah jenis restoran."""

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def show_flavors(self):
        print(f"{self.restaurant_name} has these flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


stand = IceCreamStand("Cool Corner")
stand.show_flavors()