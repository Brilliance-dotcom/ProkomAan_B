def describe_city(city, country='Indonesia'):
    """Display a message about the city and country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('Jakarta')
describe_city('Bali')
describe_city('New York', 'USA')