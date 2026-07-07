print("Welcome to Pattern & Multiplication Studio")
print("1. Square\n2. Right Triangle\n3. Number Triangle\n4. Multiplication Table")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    side = int(input("Enter a value between 2-20: "))
    for i in range(side):
        for j in range(side):
            print("#", end='  ')
        print()
elif choice == 2:
    side = int(input("Enter a value between 2-20: "))
    for i in range(side+1):
        for j in range(i):
            print("#", end=" ")
        print()
elif choice == 3:
    side = int(input("Enter a value between 2-20: "))
    for i in range(side+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
elif choice == 4:
    n = int(input("Enter the tables you want:"))
    for i in range(1,13):
        print(f"{n} x {i} = {n*i}")
else:
    print("Invalid Input")