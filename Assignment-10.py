# Wesslee Whatley; 10/3/2021; Pets

pets = [
    ('parakeet','Sweetie','blue'),
    ('parakeet','Buddy','green'),
    ('tortoise','Sully','brown'),
    ('python','Apollo','brown'),
    ('cat','Pacino','black'),
    ('cat','Latte','white')
]

for list in pets:
    print(f"{list[1]} is a {list[2]} {list[0]}.")

color = input("Please enter a color\n")
colorList = []
count = 0
for list in pets:
    if list[2] == color:
        count += 1
        name = list[1]
        colorList.append(name)
if count > 0:
    print(f"The following pets are {color}.")
    for pet in colorList:
        print(f"{pet}")
else:
    print(f"There are no pets that are {color}.")

type = input("Please enter a pet type.\n")
typeList = []
count = 0
for list in pets:
    if list[0] == type:
        count += 1
        name = list[1]
        typeList.append(name)
if count > 0:
    print(f"The following pets are {type}s.")
    for pet in typeList:
        print(f"{pet}")
else:
    print(f"There are no pets that are {type}s.")