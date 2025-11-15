#Simple To-Do List Manager
L=[]
while True:
    c=int(input("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit\nEnter your choice:"))
    if c == 1:
        t=input("Enter the task you want to add:")
        L.append(t)
        print("The task has been added successfully.")
    elif c == 2:
        if not L:
            print("No tasks added yet.")
        else:
            for i in range(len(L)):
                print(f"{i+1}. {L[i]}")
    elif c == 3:
        t = input("Enter the task you want to remove: ")
        if t in L:
            L.remove(t)
            print("The task has been removed successfully.")
        else:
            print("Task not found in the list.")
    
    elif c==4:
        print("You've exited the loop")
        break

    else:
        print("That is an invalid input.")