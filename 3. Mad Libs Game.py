#Mad Libs Game
base_story = '''Last year, (noun1) went to (noun2). What was found there was (verb1-ing)..
(noun1) found (noun3) dead in a (noun4) and went to (noun5) to (verb2).
(noun3) told (noun1) that (noun1) is (adjective1) and he needs to see (noun6) to get (verb3-past_tense)'''
print(f"This is the base story:\n{base_story}")
noun1=input("Enter the name of the main character: ")
noun2=input("This can be any place: ")
noun3=input("Enter a thing or person here: ")
noun4=input("Enter a place: ")
noun5=input("Enter another place: ")
noun6=input("This can be a person or anything from your wildest imagination: ")
verb1=input("Enter a verb in the 'ing' form: ")
verb2=input("This can be just another normal verb: ")
verb3=input("Enter a verb in past tense: ")
adjective1=input("Enter some wild adjective here: ")
print(f'''Here is your beautiful story:\n Last year, {noun1} went to {noun2}. What was found there was {verb1}..
{noun1} found {noun3} dead in a {noun4} and went to {noun5} to {verb2}.
{noun3} told {noun1} that {noun1} is {adjective1} and he needs to see {noun6} to get {verb3}''')