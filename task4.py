def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "hi":
        return "Hello! Nice to meet you."

    elif user_input == "how are you":
        return "I'm fine, thanks for asking!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "bye":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that."


print("🤖 Simple Python Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    reply = chatbot_response(user)
    print("Bot:", reply)

    if user.lower() == "bye":
        break
