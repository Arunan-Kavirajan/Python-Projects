def view_balance(balance):
    print("--------------------------------------------")
    print(f"Your Blanace is ${balance}")
    print("--------------------------------------------")

def withdraw(balance):
    n = int(input("Enter the amount to withdraw: $"))
    if n < 0:
        print("--------------------------------------------")
        print("Kindly enter a valid input.")
        print("--------------------------------------------")
    else:
        if n > balance:
            print("--------------------------------------------")
            print("Insufficient funds.")
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
            print("Withdraw Successful.")
            print("--------------------------------------------")
            return n    
        
def deposit():
    n = int(input("Enter the amount to deposit: $"))
    if n < 0:
        print("--------------------------------------------")
        print("Kindly enter a valid input.")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print("Deposit Suceessful.")
        print("--------------------------------------------")
        return n

def main():        
    balance = 0
    print("WELCOME TO OUR BANKING SYSTEM")
    while True:
        print("----------------- SERVICES -----------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit")
        print("--------------------------------------------")
        choice = int(input("Choose an option (1-4): "))
        
        if choice == 1:
            balance+=deposit()
        elif choice == 2:
            balance -= withdraw(balance)
        elif choice == 3:
            view_balance(balance)
        elif choice == 4:
            print("Thank you for using our service.")
            break

if __name__ == "__main__":
    main()