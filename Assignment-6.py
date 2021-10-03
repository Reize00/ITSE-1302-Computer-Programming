# Wesslee Whatley Fun With Strings 9/27/2021

sentence = input("Please enter a string.\n")
answer = []

for ch in sentence:
  if ch in ['a', 'e', 'i', 'o', 'u', 'y']:
    print(ch.upper(), end='')
  else:
    print(ch.lower(), end='')
print()
    
answer = sentence.split(" ")
for word in answer:
  if len(word) == 3:
    print(word)