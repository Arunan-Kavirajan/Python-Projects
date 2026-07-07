import random
balance = 1000
wins = 0
losses = 0
rounds = 0
print("="*20)
print("Welcome to Casino")
print("="*20)
while True:
    print(f"Current Balance: ${balance:.2f}")
    print("-"*30)
    print("1. Play")
    print("2. View Statistics")
    print("3. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if balance == 0:
            print("You're no longer eligible to gamble. Your balance is $0")
            break
        else:
            while True:
                print("-"*30)
                print("1. Easy (1-10)")
                print("2. Medium (1-25)")
                print("3. Hard (1-50)")
                print("-"*30)
                difficulty = int(input("Enter Difficulty (1-3): "))
                if difficulty == 1:
                    bet = float(input("Enter your bet: "))
                    if bet > balance:
                        print("Insufficient funds.")
                    elif bet < 0:
                        print("Invalid bet.")
                    else:
                        guess = int(input("Enter your guess (1-10): "))
                        number = random.randint(1,10)
                        rounds+=1
                        if guess == number:
                            print("-"*30)
                            print("You guessed correctly!!")
                            print(f"You won {bet} x 2 = {bet*2}")
                            balance = (balance-bet) + (bet*2)
                            print("-"*30)
                            wins+=1
                            break
                        else:
                            print("-"*30)
                            print("Ooopsies!! You didn't win!.")
                            print(f"The number was {number} ")
                            losses += 1
                            balance -= bet
                            print("-"*30)
                            break
                elif difficulty == 2:
                    bet = float(input("Enter your bet: "))
                    if bet > balance:
                        print("Insufficient funds.")
                    elif bet < 0:
                        print("Invalid bet.")
                    else:
                        guess = int(input("Enter your guess (1-25): "))
                        number = random.randint(1,25)
                        rounds+=1
                        if guess == number:
                            print("-"*30)
                            print("You guessed correctly!!")
                            print(f"You won {bet} x 5 = {bet*5}")
                            balance = (balance-bet) + (bet*5)
                            print("-"*30)
                            wins+=1
                            break
                        else:
                            print("-"*30)
                            print("Ooopsies!! You didn't win!.")
                            print(f"The number was {number} ")
                            losses += 1
                            balance -= bet
                            print("-"*30)
                            break
                elif difficulty == 3:
                    bet = float(input("Enter your bet: "))
                    if bet > balance:
                        print("Insufficient funds.")
                    elif bet < 0:
                        print("Invalid bet.")
                    else:
                        guess = int(input("Enter your guess (1-50): "))
                        number = random.randint(1,50)
                        rounds+=1
                        if guess == number:
                            print("-"*30)
                            print("You guessed correctly!!")
                            print(f"You won {bet} x 10 = {bet*10}")
                            balance = (balance-bet) + (bet*10)
                            print("-"*30)
                            wins+=1
                            break
                        else:
                            print("-"*30)
                            print("Ooopsies!! You didn't win!.")
                            print(f"The number was {number} ")
                            losses += 1
                            balance -= bet
                            print("-"*30)
                            break
                else:
                    print("Invalid Input")
    elif choice == 2:
        print("="*30)
        print(f"Number of rounds played: {rounds}")
        print("-"*15)
        print(f"Rounds won: {wins}")
        print("-"*15)
        print(f"Rounds Lost: {losses}")
        print("="*30)
    elif choice == 3:
        print("="*30)
        print("Thank you, visit again!")
        print("="*30)
        break
    else:
        print("Invalid Input.")