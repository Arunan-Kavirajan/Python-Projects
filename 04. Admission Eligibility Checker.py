name = input("Enter Student Name: ")
age = int(input("Enter student's age: "))
percent = float(input("Enter 12th percentage: "))
entrance = int(input("Enter entrace exam score: "))
if age >= 17:
    if percent > 60 and percent < 100:
        if entrance > 180 and entrance < 200:
            print("Eligible for Admission")
        elif entrance > 200:
            print("Invalid Input")
        else:
            print("Eligible for Management Quota")
    elif percent > 100:
        print("Invalid Input")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")