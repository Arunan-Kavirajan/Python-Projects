print("="*40)
print("Welcome to Password Strength Analyzer")
print("="*40)
pwd = input("Enter your password: ")
Length = False
has_lower = False
has_upper = False
has_digit = False
has_special = False
has_space = False
score = 0
if len(pwd) > 8:
    Length = True
for i in pwd:
    if i.isalpha():
        if i.islower():
            has_lower = True
        elif i.upper():
            has_upper = True
    elif i.isdigit():
        has_digit = True
    elif i.isspace():
        has_space = True
    else:
        has_special = True

if Length:
    score+=1
if has_lower:
    score+=1
if has_upper:
    score+=1
if has_digit:
    score+=1
if has_special:
    score+=1
if has_space:
    score+=1

if score <=2:
    print("-"*30)
    print("Your password is weak.")
    print("-"*30)
elif score <=4:
    print("-"*30)
    print("Your password is moderate.")
    print("-"*30)
else:
    print("-"*30)
    print("Your password is strong.")
    print("-"*30)

