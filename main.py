print("Welcome to Mohsin Pizza Services!")
size = input("which size of Pizza do you need? S, M, or L : ")
add_peproni = input("do you want to add peproni? Y or N : ")
extra_cheese = input("do you want extra cheese? Y or N : ")


bill = 0 

if size == "S":
  bill += 550
elif size == "M":
  bill += 1050 
elif size == "L":
  bill += 1520

if add_peproni == "Y":
  bill += 100
else:
  bill += 130

if extra_cheese == "Y":
  bill += 55

print(f"your total bill is {bill} pkr")