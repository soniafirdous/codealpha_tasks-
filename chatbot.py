   
def chatbot(name):
    print(f"Welcome {name}!")

    while True:
        user_input = input("You: ").lower()
        
        if user_input == "hello":
            print("Chatbot: Hi! 👋")
        elif user_input == "what's your name":
            print("Chatbot: I am a chatbot, what's your name?")
        elif user_input == "what do you do":
            print("Chatbot: I try to answer your prompts.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! 👋")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.Pls ask again")

chatbot("Sonia")
