# Wesslee Whatley 9/8/2021 Grade Function

import random

grades = []

def getLetter(grade):
  if grade < 60: return 'F'
  elif grade <70: return 'D'
  elif grade <80: return 'C'
  elif grade <90: return 'B'
  else: return 'A'
  
def getAverage(grades):
  return sum(grades) / len(grades)

for i in range(0, 5):
  x = random.randint(50, 100)
  grades.append(x)

for i in range(0, 5):
  print(f"Grade {i+1}: {grades[i]} {getLetter(grades[i])}")
  
average = getAverage(grades)

print(f"Average: {average} {getLetter(average)}")