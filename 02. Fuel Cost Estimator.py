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
