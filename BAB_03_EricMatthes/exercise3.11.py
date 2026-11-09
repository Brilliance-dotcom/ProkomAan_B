river1 = ("Mississippi", "Nile", "Amazon", "Yangtze", "Danube")
print(river1)
# problem with the code is instead of creating a list of rivers, it is creating a tuple of rivers.
# this will be a problem if you want to modify the list later on.
# if you use code River[0] = "Ganges" it will have an error because tuples are immutable
# to fix this is to change the parentheses to square brackets, so it will be a list instead of a tuple.
River = ["Mississippi", "Nile", "Amazon", "Yangtze", "Danube"]
River[0] = "Ganges"
print(River)
# as you can see, it fixed the problem and now you can modify the list of rivers without any errors.