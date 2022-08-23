
import random

print("Welcome to the online coin toss program!")

x=input("which side are you choosing? 'Head' or 'Tails'\n=").lower()

y=random_side=random.randint(0,1)
h="head"
t="tails"

if y==1:
  print("Head")
  if x==h:
    print("You won")
  else:
    print("Sorry, for lossing")
else:
  print("Tails")
  if x==t:
    print("\nYou won mate :)")
  else:
    print("\nSorry , you are loss :(")