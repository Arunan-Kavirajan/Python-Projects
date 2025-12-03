menu = {"burger":90.0,"pizza":170.5,"coke":40.0,"fries":60.5,"wings":200.0,"lemonade":30.5}
cart = []
total = 0
print("--------- MENU ---------")
for x,y in menu.items():
    print(f"{x:10} : ₹{y:.2f}")
print("-------------------------")

while True:
    food = input("Enter the food (Q to quit): ").lower()
    if food == 'q':
        break
    elif food in menu.keys():
        cart.append(food)
        total += menu.get(food)

print("--------- YOUR ORDER ---------")
for i in cart:
    print(i, end="  ")
print()
print(f"Total Amount: ₹{total:.2f}")
print("-------------------------------")