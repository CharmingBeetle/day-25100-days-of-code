import random

def rollDice(sides):
  dice1 = random.randint(1, sides)  
  return dice1

def rollDice6and8():
  dice6 = rollDice(6)
  dice8 = rollDice(8)
  HP = dice6*dice8
  return HP


print("Character Stats Generator")
print ()
while True:
  name = input("Name your warrior: ") 
  print("The warrior" , name , "has" , rollDice6and8() , "health points")
  print()

  playAgain = input("Do you want to generate another character? ")
  if playAgain == "yes":
    continue
  else:
    break
      