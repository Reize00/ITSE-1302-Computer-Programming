# Wesslee Whatley; 10/3/2021; Mailbox File

fname = input("Please enter a file name. (mbox-short.txt)")
try:
    fhand = open(fname)
except:
    print("That was not a valid file name.")
    exit()

count = 0

for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
        print(line[slice(50)])

print(f"Lines begin with 'Subject' {count} times.")