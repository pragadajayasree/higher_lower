
import art
import game_data
from replit import clear
import random
score = 0
def logo():
  print(art.logo)
  
def vs_logo():
  print(art.vs)

def random_name():
  return random.choice(game_data.data)

def inp():
  return input("who has more followers ? Type 'A' or 'B' ")
 
def compare(a,b):
  if a['follower_count']>b['follower_count']:
    return 'A'
  else:
    return 'B'
def names():
  a = random_name()
  b = random_name()
  while b==a:
    b=random_name()
  print(f"Compare A: {a['name']},  {a['description']}, from {a['country']} ")
  vs_logo()
  print(f"Defeat: {b['name']},  {b['description']}, from {b['country']} ")
  return a,b

def high_low(score):
  
  a,b= names()
  result=compare(a,b)
  input = inp()
  if result == input:
    score = score+1
    clear()
    logo()
    print(f"You are right! current score: {score}")
    high_low(score)
    
  else :
    clear()
    logo()
    print(f"Sorry, that's wrong . Final score: {score}")
  
logo() 
high_low(0)
    
  
  
  
  
