print("="*35)
print("        Registration Form")
print("="*35)
uname = input("Enter your Username (6-12 chars): ")
email = input("Enter your Email: ")
pwd = input("Enter a Password: ")

print("="*40)
print("          REGISTRATION REPORT")
print("="*40)

#Username
for i in uname:
    if 5>len(uname) or len(uname)>20:
        print("Username should only contain 5-20 characters.")
        break
    elif not uname[0].isalpha():
        print(" Username should start with an alphabet.")
        break
    elif i.isspace():
        print(" Username should not contain spaces.")
        break
    elif not i.isalnum() and i not in ["_"]:
        print(" Username should only contain letters, numbers, or underscores.")
        break
else:
    print("            USERNAME: VALID")

#Email

if "@" not in email:
    print("Email must contain '@'")
elif email.count("@") > 1:
    print("Email can only contain one '@'")
elif email.startswith("@") or email.endswith("@"):
    print("Email cannot start or end with '@'")
elif not email.endswith(".com"):
    print("Email must end with .com")
else:
    print("            EMAIL: VALID")

#Password
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
    print("            PASSWORD: WEAK")
elif score <=4:
    print("            PASSWORD: MODERATE")
else:
    print("            PASSWORD: STRONG")

print("="*40)



