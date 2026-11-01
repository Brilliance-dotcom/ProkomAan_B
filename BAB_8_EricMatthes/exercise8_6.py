def city_country(city, country):
    """Display a message about the city and country."""
    return f"{city.title()}, {country.title()}"

place1 = city_country('Jakarta', 'Indonesia')
place2 = city_country('New York', 'USA')
place3 = city_country('Tokyo', 'Japan')

print(place1)
print(place2)   
print(place3)