import random
quotes = ["ye","nah bro","wth","thats suuuuuuuus","bro this kid","I stg","get help", "chill","die","su","su kid", "I stg, bro this kid...","who asked","haram"]
print("Welcome to MhadiAI, the most advanced and accurate chatbot that replies with things mhadi would say!")
print("Type 'quit' to exit")
while True:
    userInput = input("You: ")
    if userInput == "quit":
        break
    else:
        print("MhadiAI: " + random.choice(quotes))
print("Thanks for using MhadiAI!")
