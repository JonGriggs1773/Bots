from jokes_db import jokes
import random
import time



def joke_bot(list):
    user_input = input("Do you wanna hear a joke? Answer y/n:  ")
    if user_input == "y":
        joke = random.choice(list)
        print(joke['setup'])
        time.sleep(3)
        print(joke['punchline'])
        time.sleep(3)
        joke_bot(list)
    else:
        print("Awwww okay loser :(")

joke_bot(jokes)