prompt = "welcome to our pizzaria, what topping would you like on your pizza ?" 
prompt += "\n(enter 'quit' when you are finished) "
n = 0
while True:
    topping = input(prompt)
    n += 1
    print("===============================================================")
    if topping == 'quit':
        break
    else:
        print(f"we will add {topping} to your pizza !")
        print("===============================================================")
    if n == 5:
        print("You have reached the maximum number of toppings allowed (5).")
        print("===============================================================")
        break
    