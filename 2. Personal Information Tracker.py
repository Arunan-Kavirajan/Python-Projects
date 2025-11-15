name = input("Enter your Full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
student = bool(input("Are you a student? Skip if you're not. "))

print("Profile Review")
print(f"Name: {name}\nAge: {age}\nHeight: {height}ft which is {round(height*30.48)}cm")
print("Student: Yes" if student==True else "Student: No")