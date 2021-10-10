# Wesslee Whatley Fun With Strings 9/27/2021

sentence = input("Please enter a string.\n")
answer = []

for ch in sentence:
  if ch in ['a', 'e', 'i', 'o', 'u', 'y']:
    print(ch.upper(), end='')
  else:
    print(ch.lower(), end='')
print()

start = 0
    
for x in range(0, len(sentence)):
  if sentence[x] == " ":
    slices = slice(start, x)
    answer.append(sentence[slices])
    start = x+1

slices = slice(start, len(sentence))
answer.append(sentence[slices])
print()

for word in answer:
  if len(word) == 3:
    print(word)