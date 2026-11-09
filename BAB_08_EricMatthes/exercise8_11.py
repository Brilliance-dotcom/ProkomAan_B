from BAB_8_EricMatthes.exercise8_10 import send_messages

messages = [
    "Hello,how's life ?", 
    "Doing good, appreciate it", 
    "What about you?", 
    "I'm great, thanks twin"]

sent_messages = send_messages(messages[:])
print("\nOriginal messages list:")
print(messages)
print("\nSent messages:")
print(sent_messages)
