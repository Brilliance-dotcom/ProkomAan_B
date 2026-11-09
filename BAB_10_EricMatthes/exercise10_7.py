print("Enter 'q' at any time to quit.")

while True:
    first_number = input("\nEnter the first number: ")
    if first_number == "q":
        break

    second_number = input("Enter the second number: ")
    if second_number == "q":
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, you need to enter numbers, not text.")
    else:
        print(f"The sum is {total}")