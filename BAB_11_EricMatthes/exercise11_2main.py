def get_city_country(city, country, population=""):
    """Return a string like 'Santiago, Chile' or
    'Santiago, Chile – population 5000000'."""
    if population:
        formatted = f"{city}, {country} – population {population}"
    else:
        formatted = f"{city}, {country}"
    return formatted.title()