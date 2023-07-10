from quoteDB import quotes
import random
import time


def quote_bot(list):
    user_input = input("I have some famous quotes here, wanna hear one? Answer y/n:  ")
    if user_input == "y":
        quote = random.choice(list)
        print(quote['text'], " -", quote['author'] )
        time.sleep(3)
        print("What a gret quote!!!")
        quote_bot(list)
    else:
        print("Fine loser :(")

quote_bot(quotes)