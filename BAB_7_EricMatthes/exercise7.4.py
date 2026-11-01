prompt = "welcome to our pizzaria, what topping would you like on your pizza ?" 
prompt += "\n(enter 'quit' when you are finished) "
while True:
    topping = input(prompt)
    print("===============================================================")
    if topping == 'quit':
        break
    else:
        print(f"we will add {topping} to your pizza !")
        print("===============================================================")
    