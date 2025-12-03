import random
l = int(input("Enter the lower limit: "))
u = int(input("Enter the upper limit: "))
number = random.randint(l,u+1)
guesses = 0
print("Welcome to the Number Guessing Game!")
print(f"Enter a digit between {l} and {u}")
print("---------------------------------------------------------------")
while True:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        if int(guess) == number:
            guesses += 1
            print("You guessed the number right!!")
            print(f"It only took you {guesses} tries!")
            break
        else:
            guesses +=1
            print("Oopsie. Try again")
    else:
        print("Invalid Input.")
        print(f"Please enter a digit between {l} and {u}")