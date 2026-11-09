import unittest
from exercise11_2main import get_city_country


def test_city_country():
    """Does a city and country like 'Santiago, Chile' work?"""
    formatted_name = get_city_country("santiago", "chile")
    assert formatted_name == "Santiago, Chile"


def test_city_country_population():
    """Does 'Santiago, Chile – population 5000000' work?"""
    formatted_name = get_city_country("santiago", "chile", population=5000000)
    assert formatted_name == "Santiago, Chile – population 5000000"

if __name__ == '__main__':
  unittest.main()