questions = ("Which planet is known as the 'Red Planet'?","What is the largest ocean on Earth?","Who painted the famous artwork 'Mona Lisa'?","Which gas do plants primarily absorb from the atmosphere for photosynthesis?","What is the capital city of Australia?")
answers = ("C","C","C","C","D")
guesses = [["A. Jupiter","B. Venus","C. Mars","D. Saturn"],["A. Atlantic Ocean","B. Indian Ocean","C. Pacific Ocean","D. Arctic Ocean"],["A. Vincent van Gogh","B. Pablo Picasso","C. Leonardo da Vinci","D. Claude Monet"],["A. Oxygen","B. Nitrogen","C. Carbon Dioxide","D. Hydrogen"],["A. Sydney","B. Melbourne","C. Brisbane","D. Canberra"]]
Number = 0
score = 0

print("QUIZ TIME")
for question in range(len(questions)):
    Number+=1
    print("------------------------------------------------------------------")
    print(f"{Number}. {questions[question]}")
    for guess in guesses[Number-1]:
        print(guess)
    answer=input("Enter your answer: ").upper()
    if answer == answers[Number-1]:
        print("Thats the corrent answer")
        score+=1
    else:
        print(f"Thats not the correct answer.\nThe corrent answer is option {answers[Number-1]}")
        
print("------------------------------------------------------------------") 
print("RESULT")       
print(f"You got {score}/{len(questions)} correct.")
print(f"Your score is {int((score/len(questions)*100))}%")