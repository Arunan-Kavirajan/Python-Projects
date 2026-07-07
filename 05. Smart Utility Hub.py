print("===== Utility Hub =====")
print("1. Number System Converter")
print("2. Bill Calculator")
print("3. Fuel Cost Estimator")
print("4. Exit")
choice = int(input("Choose your tool: "))
match choice:
    case 1:
        decimal = int(input("Enter an Decimal: "))
        print("="*20)
        print("NUMBER SYSTEM CONVERTER")
        print("="*20)
        print(f"Decimal : {decimal}")
        print(f"Binary: {bin(decimal)}")
        print(f"Octal: {oct(decimal)}")
        print(f"Hexadecimal: {hex(decimal)}")
        print("="*20)
    case 2:
        c_name = input("Enter customer's name: ")
        n = int(input("Enter the number of products purchased: "))
        total = 0
        product = []
        q = []
        p = []
        for i in range(n):
            p_name = input("Enter product's name: ")
            product.append(p_name)
            quantity = int(input("Enter the quantity: "))
            q.append(quantity)
            price = int(input("Enter price: "))
            p.append(price)
            product_price = price * quantity
            total += product_price
        gst = (total * 18)/100
        print("-" * 30)
        print(f"Customer name: {c_name}")
        print("PRODUCTS")
        for i in range(n):
            print(f"{product[i]}    {q[i]} x ₹{p[i]}")
        print(f"Total: ₹{total}")
        print(f"GST(18%) ₹{gst}")
        print(f"Grand Total: ₹{total + gst}")
        print("-" * 30)
    case 3:
        distance = int(input("Enter distance in km: "))
        fuel = int(input("Enter fuel cost (₹/L): "))
        mileage = int(input("Enter Vehicle Mileage (km/L): "))
        passengers = int(input("Enter number of passengers:" ))
        fuel_need = distance/mileage
        fuel_cost = fuel_need*fuel
        split = fuel_cost/passengers
        print(f"Distance: {distance}km")
        print(f"Fuel needed: {fuel_need}L")
        print(f"Fuel cost: ₹{fuel_cost}")
        print(f"Price each should pay: ₹{split}")

    case 4:
        print("Thanks for using our system")

    case _:
        print("Invalid Input")