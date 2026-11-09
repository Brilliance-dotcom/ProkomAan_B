#exercise8_2.py
def favorite_book(
        title):
    """Display a message about the favorite book."""
    print(f"One of my favorite books is '{title.title()}'.")

favorite_book('Alice in Wonderland')
#exercise8_7.py
def describe_city(
        city, country='Indonesia'):
    """Display a message about the city and country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('Jakarta')
describe_city('Bali')
describe_city('New York', 'USA')
#exercise8_9
messages = [
    "Hello,how's life ?", 
    "Doing good, appreciate it", 
    "What about you?", 
    "I'm great, thanks twin"]
def show_messages(
        messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

show_messages(messages)