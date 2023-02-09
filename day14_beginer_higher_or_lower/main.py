import os
import json
import random
from typing import List
from art import logo, vs


used = []


def details(name, follower_count, description, country):
    return f"{name}, a {description}, from {country}."


def get_random_pearson(data: List[dict], A):
    if not A: A = random.choice(data)
    B = random.choice(data)
    while B == A or B in used:
        B = random.choice(data)
    used.append(B)
    return A,B
    
    
def start_game():
    with open('game_data.json') as f:
        data = json.load(f)
        
    score = 0
    A = None
    
    while True:
        os.system('cls')
        print(logo)
        if score: print("You are right! Current Score: ", score)
        A, B = get_random_pearson(data, A)
        print("Compare A:", details(**A))
        print(vs)
        print("Compare B:", details(**B))
        response = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (response == 'a' and A['follower_count'] >= B['follower_count']) :
            score +=1
        elif (response == 'b' and B['follower_count'] >= A['follower_count']):
            A = B
            score +=1
        else:
            break
        if score == 50:
            os.system('cls')
            print(logo)
            print("You have got all guesses correct! Your Score : 50")
            return
        
    os.system('cls')
    print (logo)
    print("Sorry, that's wrong! Final score :", score)


if __name__ == "__main__":
    start_game()