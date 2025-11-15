#Smart Admission Eligibility Checker
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
gpa = float(input("Enter your school GPA: "))
eligibility = True
print("Profile Review:")
print(f"Your name is {Name}")
if Age>17 and Age<25:
    print("Your age is in the eligibility range.")
else:
    print("Your age is not in the eligibility range.")
    eligibility=False
if gpa<6:
    print("Your gpa makes you unqualified.")
    eligibility=False
else:
    print("Your gpa is eligible")
print("You are eligible to apply." if eligibility == True else "You're not eligible to apply.")