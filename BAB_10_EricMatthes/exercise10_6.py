first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

try:
    total = int(first_number) + int(second_number)
except ValueError:
    print("Sorry, you need to enter numbers, not text.")
else:
    print(f"The sum is {total}")