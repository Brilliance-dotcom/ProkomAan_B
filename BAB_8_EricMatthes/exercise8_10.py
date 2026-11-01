messages = [
    "Hello,how's life ?", 
    "Doing good, appreciate it", 
    "What about you?", 
    "I'm great, thanks twin"]
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)
def send_messages(messages):
    """Simulate sending each message in the list."""
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
    return sent_messages

sent_messages = send_messages(messages[:])  
print("\nOriginal messages list:")
print(messages)  

print("\nSent messages:")
print(sent_messages)