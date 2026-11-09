import unittest
from exercise11_1main import get_city_country


def test_city_country():
    """Does a city and country like 'Santiago, Chile' work?"""
    formatted_name = get_city_country("santiago", "chile")
    assert formatted_name == "Santiago, Chile"

if __name__ == '__main__':
  unittest.main()