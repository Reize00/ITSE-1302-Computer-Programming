# Wesslee Whatley; 10/3/2021; Days of Week

choice = 0

while choice < 1 or choice > 7:
    try:
        choice = int(input("Please enter a number 1-7."))
    except:
        print("Please enter a valid number.")

days = ["Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
    ]

print(days[choice-1])