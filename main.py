from random import choice
from game_data import data
from art import logo, vs
from replit import clear

def format_data(acc):
    return f"{acc['name']}, a {acc['description']} from {acc['country']}"

def check_answer(answer, a, b):
    return (a['follower_count'] > b['follower_count'] and answer == 'a') or (b['follower_count'] > a['follower_count'] and answer == 'b')

game_over = False
score = 0

a = choice(data)

while not game_over:
    print(logo)
    print(f"Compare A: {format_data(a)}")
    print(vs)

    b = choice(data)
    while b == a:
        b = choice(data)

    print(f"Against B: {format_data(b)}")
    answer = input("Who has more followers, type 'A' or 'B': ").lower()
    is_correct = check_answer(answer, a, b)

    if is_correct:
        score += 1
        a = b 
        clear()
    else:
        game_over = True

clear()
print(logo)
print(f"Sorry, that's wrong. Final score is: {score}")
