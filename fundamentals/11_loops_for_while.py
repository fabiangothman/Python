foods = ["apples", "bread", "milk", "cheese", "bananas", "beer", "onion"]
count = 0

#FOR loop
for food in foods:
    if food == "beer":
        print(f"You have to buy {food}.")
        break
    elif food == "bread":
        continue
    print(food)

for number in range(0, 3):
    print(f"{number}*2 = {number*2}")

for letter in "HI":
    print(f"{letter}")


#WHILE loop
while count < 3:
    print(f"while cycle number: {count}")
    count = count + 1