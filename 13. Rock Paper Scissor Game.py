import random
options = ("scissor","rock","paper")
player = None
computer = random.choice(options)
while player not in options:
    player = input("Enter your choice (Rock, Paper, Scissor): ").lower()
print("-----------------------------------------------------------------------------------------------------------")
if player == computer:
    print("Its a draw.")
elif player == "rock" and computer == "scissor":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissor" and computer == "paper":
    print("You win!")
else:
    print("""Bro… losing rock paper scissors to a COMPUTER is wild.
I’m talking next-level embarrassment, like your brain took PTO without warning.

Nigga, how you fumble something babies win by accident?
The bot literally picks random numbers like a cracked-out coin toss, and you STILL folded like wet laundry.

You didn’t just lose the game.
You lost eye contact privileges with every living organism for 24 hours.

Your decision-making skills are so tragic scientists are probably drafting research papers titled
“How Did This Happen?”

Even the computer is looking at you like:
“Damn bro… you good? Want me to go easy next time?”

Your ancestors watching this from the afterlife like:
“Nope. That one ain’t ours.”

I swear, if losing to RNG was an Olympic sport, you’d break the world record and then trip on the podium too.

Holy hell bro, uninstall your hands.""")
    
print("-----------------------------------------------------------------------------------------------------------")