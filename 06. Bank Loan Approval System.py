loan = int(input("Enter your loan amount: "))
age = int(input("Enter your age: "))
print("Employment Type")
print("1. Salaried")
print("2. Self Employed")
print("3. Business Owner")
print("4. Other")
job = int(input("Choose (1-4): "))
exp = int(input("Enter Years of Experience: "))
score = int(input("Enter Credit Score: "))
salary = int(input("Enter  your Monthly Salary:"))
preloan = input("Pre-Existing Loans? Yes or No: ")
if 21<age<60:
    if job == 1 or job == 2 or job == 3:
        if (job == 1 and exp >= 1) or (job == 2 and exp >= 2) or (job == 3 and exp >= 3):
            if 650 <= score <=900:
                if (25000<=salary<=49999 and loan <= 500000) or (50000<=salary<=100000 and loan <= 1000000) or (salary>100000 and loan<= 50_00_000):
                    if preloan.lower() == "yes":
                        if loan > 10_00_000:
                            print("Loan rejected due to pre-existing loan.")
                        else:
                            print(f"Loan amount of ₹{loan} has been approved.")
                    elif preloan.lower() == "no":
                        print(f"Loan amount of ₹{loan} has been approved.")
                    else:
                        print("Invalid Input.")
                else:
                    print("Loan rejected due to insufficient salary for your laon amount.")
            elif 300>score or score>900:
                print("Invalid Input")
            else:
                print("Loan rejected due to insufficient credit score.")
        elif exp < 0 or exp > 40:
            print("Invalid Input.")
        else:
            print("Loan rejected due to lack of experience.")
    elif job == 4:
        print("Loan rejected due to employment type.")
    else:
        print("Invalid Input.")
else:
    print("Loan rejected since your age is out of range.")
