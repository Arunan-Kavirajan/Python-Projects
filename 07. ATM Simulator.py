balance = 10000
while True:
    print("="*20)
    print("        ATM")
    print("="*20)
    print("1. Deposit")
    print("2. View Balance")
    print("3. Withdraw")
    print("4. Exit")
    print("="*20)
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        dep = float(input("Enter your deposit amount: $"))
        balance+=dep
        print("-"*30)
        print(f"${dep:.2f} has been deposited.")
        print("-"*30)
    elif choice == 2:
        print("-"*30)
        print(f"Current Balance: ${balance:.2f}")
        print("-"*30)
    elif choice == 3:
        wit = float(input("Enter withdraw amount: $"))
        if balance-wit < 0:
            print("-"*30)
            print("Insufficient Funds.")
            print("-"*30)
        else:
            balance-=wit
            print("-"*30)
            print(f"Withdraw of ${wit:.2f} was successful\nKindly collect the cash")
            print("-"*30)
    elif choice == 4:
        print("-"*30)
        print("Thanks for using our service")
        print("-"*30)
        break
    else:
        print("-"*15)
        print("Invalid Input.")
        print("-"*15)