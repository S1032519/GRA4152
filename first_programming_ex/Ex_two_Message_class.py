"""
The object of this task is to create a program that simulates sending and receiving emails. We want to store the total number of
emails sent and save a a log of the message sent.

The methods are:
    - append, param =(self, text), this method appends text to the message_body and records the message.

    - toString, param =(self), this method creates the string but uses "\n" to add a line after sender email, receiver email, and message
    body. It was somewhat unclear if the "\n" should be used since the exercise said "make one long string" but it alos said "like this" and used "\n" itself.

    - log_messages, param =(self), this method increases the count for sent messages. It also checks whether the sender is logged, if it is not
    then we log the message according to the task.
"""

class Message: ## Defining the class Message

    ## Adding class variables
    _no_messages = 0 ## counting variables to count sent messages
    _log = {} ## log variables to store messages

    def __init__(self, sender, recipient): ## Constructor
        self._sender = sender ## Instance variable which takes an object of type str
        self._recipient = recipient ## Instance variable which takes an object of type str
        self._message_body = "" ## Instance variable which takes an object of type str

    def append(self, text):
        self._message_body += text + " " ## Appending the message
        self.log_messages() ## This is invoked after a message is appended

    def toString(self):
        return f"From: {self._sender}\nTo: {self._recipient}\n{self._message_body.strip()}" ## Creates the message string incl sender and receiver, with new line between.
    
    def log_messages(self):
        Message._no_messages += 1 ## Updates the number of sent messages by one

        if self._sender not in Message._log: ## Checking if the sender allready is in the dictionary (is a key)
            Message._log[self._sender] = {} ## If the sender is not in the dictionary then, create an empty dictionary for the sender
        Message._log[self._sender][self._recipient] = self._message_body ## Updates nested dictionary


## Test
message1 = Message("Harry Morgan", "Rudolf Reindeer")
message1.append("Hi, how are you?")
print(message1.toString())
    
message2 = Message("user1test@gmail.com", "user2test@hotmail.com")
message2.append("Hi user2, testing testing.")
print(message2.toString())
    
# Displaying class variables
print("Total number of messages:", Message._no_messages)
print("Log of messages:", Message._log)    