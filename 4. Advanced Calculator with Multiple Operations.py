#Advanced Calculator with Multiple Operations
import math
import cmath
operation = input("Enter an operation of choice (! - factorial, + - addition,- - subtraction, * - multiplicaiton, ** - exponent, / - division, // - floor divison, % - modulus, # - root): ")
if operation == "!":
    fac=1
    a=int(input("Enter a number: "))
    if a<0:
        print("Invalid input. Enter a positive value")
    else:
        for i in range(1,a+1):
            fac*=i
        print(f"Factorial of {a} is {fac}")
        
elif operation == "+":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    print(f"The addition of {a} and {b} is {a+b}")
    
elif operation == "-":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    print(f"The subtraction of {a} and {b} is {a-b}")
    
elif operation == "*":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    print(f"The multiplication of {a} and {b} is {a*b}")
    
elif operation == "**":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    print(f"The power of {b} on {a} is {a**b}")
    
elif operation == "/":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    print(f"The division of {a} and {b} is {a/b}")
    
elif operation == "//":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    print(f"The floor division of {a} and {b} is {a//b}")
    
elif operation == "%":
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    print(f"The modulus of {a} and {b} is {a%b}")
    
elif operation == "#":
    a=float(input("Enter a number: "))
    if a<0:
        print(f"The square root of {a} is {cmath.sqrt(a)}")
    else:
        print(f"The square root of {a} is {math.sqrt(a)}")
else:
    print("Invalid input.")
        