
import Functions
import time


now=time.strftime("%b %d, %Y %H:%M")
print(f"Today is: {now} \n")
while True:
    user_action=input("Please type add(with to-do description), show, edit(to-do list number), complete (to-do list number) or exit: ")
    x=1
    #removes spaces before or after the user input string
    user_action=user_action.strip()

    if user_action.startswith("add"):
            todo= user_action[4:]

            #creates input file object, reads content to string and closes
            todos=Functions.get_todos()

            #appends the user input to the string that was read from the file (file content)
            todos.append(todo+ "\n")

            #opens the file to write. adds to the file the string with the added input and closes file.
            # with open("todos.txt","w") as output_todos_file:
            #     output_todos_file.writelines(todos)

            Functions.write_todos(todos)
            
    elif user_action.startswith("show"):

            todos=Functions.get_todos()
            
            #makes the list strings better to be viewed on the command line
            new_todos=[item.strip("\n") for item in todos]
            for index,item in enumerate(new_todos):
                print(f"{index+1}-{item}")

            
        
    elif user_action.startswith("edit"):
            
        try:
            todos=Functions.get_todos()

            #list_number= int(input("Enter the number of the item in the list that you would like edit: "))
            #list_number= list_number-1
            list_number=int(user_action[5:])

            new_todo=input("Enter new to do item: ")
            todos[list_number-1]=new_todo + "\n"

            Functions.write_todos(todos)

        except ValueError:
            print("Invalid input. Please enter a number in the list to edit\n")
            continue


    elif user_action.startswith("complete"):
        try:
            #completed_number=int(input("Enter the number of the item in the list that you would like to mark completed: "))
            completed_number=int(user_action[9:])
            todos.pop(completed_number-1)

            Functions.write_todos(todos)
        
        except IndexError:
            print("Invalid list item number. Please enter a list number within the list.\n")
            continue

    elif user_action.startswith("exit"):
            #break ends the loop manually
            break
   
    
    
print ("Bye!")