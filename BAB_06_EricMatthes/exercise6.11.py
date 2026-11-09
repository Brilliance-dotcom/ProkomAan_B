cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '520,000',
        'fact': 'Running through surakarta is Bengawan Solo river',
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'the most populous metropolitan area in the world',
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'home to the Eiffel Tower',
    },
}

for city, info in cities.items():
    print("===============================================================")
    print(f"City        : {city.title()}")
    print(f"Country     : {info['country'].title()}")
    print(f"Population  : {info['population']}")
    print(f"Fact        : {info['fact']}")
print("===============================================================")

