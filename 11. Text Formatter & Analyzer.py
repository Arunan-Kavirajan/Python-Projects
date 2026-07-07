print("="*40)
print("  Welcome to Text Formatter & Analyzer")
print("="*40)
text = input("Enter your text: ")
vowels = 0
cons = 0
for i in text.lower():
    if i.isalpha():
        if i in ['a','e','i','o','u']:
            vowels+=1
        else:
            cons+=1
while True:
    print("-"*35)
    print("        AVAILABLE SERVICES")
    print("-"*35)
    print('''
    1. Character Count
    2. Word Count
    3. Convert to Uppercase
    4. Convert to Lowercase
    5. Convert to Title Case
    6. Reverse Text
    7. Count Vowels
    8. Count Consonants
    9. Check Palindrome
    10. Exit''')
    print("-"*35)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("-"*35)
            print(f"Character Count: {len(text)}")
        case 2:
            print("-"*35)
            print(f"Word Count: {len(text.split())}")
        case 3:
            print("-"*35)
            print(f"Text in uppercase: {text.upper()}")
        case 4:
            print("-"*35)
            print(f"Text in lowercase: {text.lower()}")
        case 5:
            print("-"*35)
            print(f"Text in titlecase: {text.title()}")
        case 6:
            print("-"*35)
            print(f"Text in reverse: {text[ : :-1]}")
        case 7:
            print("-"*35)
            print(f"Number of vowels: {vowels}")
        case 8:
            print("-"*35)
            print(f"Number of consonants: {cons}")
        case 9:
            print("-"*35)
            if text.lower() == text[ : :-1].lower():
                print("It is palindrome")
            else:
                print("It is not palindrome")
        case 10:
            print("-"*35)
            print("Thank you for using our service.")
            print("-"*35)
            break
        case _:
            print("-"*35)
            print("Invalid Input")
            print("-"*35)