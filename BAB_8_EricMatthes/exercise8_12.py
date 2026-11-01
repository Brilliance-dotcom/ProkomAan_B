def make_sandwich(*ingredients):
    """Print the sandwich order."""
    print("Your sandwich includes the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese', 'mustard', 'pickles')
make_sandwich('peanut butter', 'jelly')
