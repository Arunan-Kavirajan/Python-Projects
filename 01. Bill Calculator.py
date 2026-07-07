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