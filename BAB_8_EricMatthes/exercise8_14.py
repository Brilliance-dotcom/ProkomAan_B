def car_info(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = car_info('nissan', 'Gtr', color='white', tow_package=True)
print(car)