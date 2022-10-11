import random as rd

rand = rd.randint(1,10)
user = int(input("Input the number (range 1-10) : "))

if user == rand:
  print("Correct")
else:
  print("Try Again")
