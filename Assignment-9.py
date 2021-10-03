# Wesslee Whatley; 10/3/2021; English To French

eng = ""

language = {
    "one":"une",
    "two":"deux",
    "three":"trois",
    "four":"quatre",
    "five":"cinq"
}

while eng not in language:
    eng = input("Please enter a number one through five in English.\n")
    if eng not in (language):
        print(f"{eng} is not in the dictionary!")

print(f"{eng} in French is {language[eng]}")