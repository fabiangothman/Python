name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "Carter":
        print(f"You are {name} {lastname}")
    else:
        print(f"You are not {name} {lastname}")
else:
    print(f"You are not {name}")


num = float(input("Insert your num: "))
if num <= 2:
    print(f"{num} is between (-oo, 2]")
elif num > 2 and num <=10:
    print(f"{num} is between (2, 10]")
elif not (num == 20):
    print(f"{num} is not equal to 20")
elif num > 30 or num <= 40:
    print(f"{num} is greater than 30 or less than 40")
else:
    print("Nothing")