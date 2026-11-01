function = {'for' : 'repeats a block of code once for each item in a sequence', 
                   'if' : 'tests a condition and executes a block of code if the condition is true', 
                   'append' : 'adds an item to the end of a list', 
                   'upper' : 'converts a string to uppercase', 
                   'else' : 'executes a block of code if the condition in an if statement is false',
                   'title' : 'converts the first character of each word to uppercase',
                   'elif' : 'tests a condition and executes a block of code if the condition is true, otherwise executes another block of code',
                   'pop' : 'removes the last item from a list and returns it',
                   'print' : 'outputs a message to the console',
                   'lower' : 'converts a string to lowercase'}
for function, meaning in function.items():
    print(f"\n{function}")
    print(f"- {meaning}")