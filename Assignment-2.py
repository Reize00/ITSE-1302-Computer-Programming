# Wesslee Whatley; 08/31/2021; Payroll

# First employee info
name1 = input("Please enter employee name: ")
hour1 = float(input("Please enter hours worked: "))
wage1 = float(input("Please enter hourly wage:"))

# Second employee info
name2 = input("Please enter second employee name: ")
hour2 = float(input("Please enter hours worked: "))
wage2 = float(input("Please enter hourly wage: "))

# Calculating gross pay and total
gross1 = round((hour1 * wage1),2)
gross2 = round((hour2 * wage2),2)
total = gross1 + gross2

# Printing responses
print("{}'s gross pay was ${:.2f}.".format(name1, gross1))
print("{}'s gross pay was ${:.2f}.".format(name2, gross2))
print("Make sure you have ${:.2f} in the bank!".format(total))