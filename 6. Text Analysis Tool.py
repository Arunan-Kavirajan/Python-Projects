#Text Analysis Tool
s=input("Enter a string of your choice: ")
f=int(input("Choose the function you want yo use:\nCharacter Count - 1\nLength of String - 2\nNumber of words - 3\nChange the Text Case - 4\nAccess a part of the string - 5\nEnter your choice: "))
if f==1:
    c=input("Enter the character you want the count of (Case sensitive): ")
    print(f"The count of '{c}' in '{s}' is {s.count(c)}")
    
elif f==2:
    print(len(s))
    
elif f==4:
    c=int(input("1.Upper-Case\n2.Lower-Case\n3.Title-Case\nEnter the case of your choice:"))
    if c==1:
        print(s.upper())
    elif c==2:
        print(s.lower())
    elif c==3:
        print(s.title())
    else:
        print("Invalid input.")
        
elif f==3:
    print(len(s.split()))
    
elif f==5:
    a=int(input("Enter the index of first char: "))
    b=int(input("Enter the index of second char: "))
    if a<b:
        print(s[a:b+1])
    else:
        print(s[a-1:b:-1])

else:
    print("Invalid input.")