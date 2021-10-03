# Wesslee Whatley; 09/08/2021; Better Payroll

def grossPay (hour, wage): #returns gross pay
  pay = 0;
  if hour > 40:
    overtime = hour - 40
    pay += overtime * (wage * 1.5)
    hour = 40
  pay += hour * wage
  return pay

try:
  # First employee info
  name1 = input("Please enter employee name: ")
  hour1 = float(input("Please enter hours worked: "))
  wage1 = float(input("Please enter hourly wage:"))

  # Second employee info
  name2 = input("Please enter second employee name: ")
  hour2 = float(input("Please enter hours worked: "))
  wage2 = float(input("Please enter hourly wage: "))
  
  # Calculating gross pay and total
  gross1 = round(grossPay(hour1, wage1),2)
  gross2 = round(grossPay(hour2, wage2),2)
  total = gross1 + gross2
  
  # Printing responses
  print(f"{name1}'s gross pay was ${gross1:.2f}")
  print(f"{name2}'s gross pay was ${gross2:.2f}")
  print(f"Make sure you have ${total:.2f} in the bank!")
except:
  print("Please input numbers for the hour and wage.")