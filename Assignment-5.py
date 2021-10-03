# Wesslee Whatley 9/18/2021 Grade Function with Loops

import random

number = 0

while number < 3 or number > 20:
  try:
    number = int(input("Please enter an integer between 3 and 20."))
  except:
    print("Invalid input, please try again.")

grades = []

def getLetter(grade):
  if grade < 60: return 'F'
  elif grade <70: return 'D'
  elif grade <80: return 'C'
  elif grade <90: return 'B'
  else: return 'A'
  
def getAverage(grades):
  return sum(grades) / len(grades)

for i in range(0, number):
  x = random.randint(50, 100)
  grades.append(x)

for i in range(0, number):
  print(f"Grade {i+1}: {grades[i]} {getLetter(grades[i])}")
  
average = getAverage(grades)

print(f"Average: {average:.2f} {getLetter(average)}")