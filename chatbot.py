print("Hello!I am your AI chatbot!\n")
print("Type bye to exit\n")
while True:
    user = input("You:")
    user = user.lower().strip()
    if user in ["hello","hi","hey"]:
        print("Bot: Hi there!")
    elif user == "how are you?":
        print("Bot:I am doing great!")
    elif user == "what is your name?":
        print("Bot:I am AIChatBot")
    elif user == "goodmorning":
        print("Bot:GoodMorning!")
    elif user == "goodafternoon":
        print("Bot:GoodAfternoon!")
    elif user == "goodevening":
        print("Bot:GoodEvening!")
    elif user == "goodnight":
        print("Bot:GoodNight!")
    elif user == "thankyou":
        print("Bot:You are Welcome!")
    elif user == "bye":
        print("Bot:Goodbye!")
        break
    else:
        print("Bot:Sorry,I don't understand.")
