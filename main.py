import art
import random
import game_data
from replit import clear

#generate a random account from the game_data. 
def random_person():
  return random.choice(game_data.data)

a = random_person()
b = random_person()
score = 0


#format the account
def format(person):
  details = print(f"{person['name']}, {person['description']}, {person['country']} ")
  return details

def ask_guess():
  guess = input("Choose which has more followers: 'A' or 'B' ").lower()
  return guess


def correct_guess(a,b,guess):
  f_count_a = a['follower_count']
  f_count_b = b['follower_count']
  if f_count_a > f_count_b: 
    return guess == "a" 
  else:
    return guess == "b"

def play_game(a,b,score):
  correctly_guessed = True
  while correctly_guessed:
    print(art.logo)
    print("Choice A:")
    format(a)
    print(a['follower_count'])
    print(art.vs)
    print("Choice B:")
    format(b)
    print(b['follower_count'])
    guess = ask_guess()
    correctly_guessed = correct_guess(a,b,guess)
    if not correctly_guessed:
      print(f"Wrong your score is {score}")
      break
    else:
      a = b
      b = random_person()
      format(b)
      clear()
      print(f"Correct, your score is {score+1}")
      
    return play_game(a,b,score+1)
   
    
 
  
play_game(a,b,score)     
