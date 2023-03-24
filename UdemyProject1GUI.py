import Functions
import PySimpleGUI as gui
import time
import os 


if not os.path.exists("todo.txt"):
    with open("todos.txt","w") as file:
        pass

program_theme= gui.theme("GreenTan")

window_label= gui.Text("Please enter a to-do item: ")
window_input= gui.InputText(tooltip="Enter to do here", key="todo_item_add")
#add_button= gui.Button("Add")
add_button= gui.Button("Add", tooltip="Select to add to do item", mouseover_colors="LightBlue2")

#to create a list of selectable options in a text box
#key for this element is the same as the event when an item in the list is selected
list_of_todos= gui.Listbox(values=Functions.get_todos(), key="todo_show_list", enable_events=True, 
                            size=[45,10])

edit_button= gui.Button("Edit")

# complete_button= gui.Button("Complete")
complete_button= gui.Button("Complete", tooltip="Select to complete an item. Removes the item from the list", mouseover_colors="LightBlue2")
exit_button= gui.Button("Exit")

clock= gui.Text(" ", key="clock_key")


todoprogram_window= gui.Window(title="Simple To-List", 
                            layout=[ [clock],
                                     [window_label,window_input,add_button],
                                     [list_of_todos,edit_button,complete_button],
                                     [exit_button]], 
                                        font=("Arial",14))


while True:
    
    user_event,user_input_values= todoprogram_window.read(timeout=10)
    todoprogram_window["clock_key"].update(value=time.strftime("%b %d %Y %H:%M :%S"))

    match user_event:
        case "Add":
            todos= Functions.get_todos()

            new_todo_item=user_input_values["todo_item_add"] + "\n"
            todos.append(new_todo_item)
            
            Functions.write_todos(todos)
            todoprogram_window["todo_show_list"].update(todos)
        

        case "Edit":
            try:
                todo_to_edit= user_input_values["todo_show_list"][0]
                new_todo= user_input_values["todo_item_add"]

                todos= Functions.get_todos()
                edit_index= todos.index(todo_to_edit)
                todos[edit_index]=new_todo

                Functions.write_todos(todos)
                todoprogram_window["todo_show_list"].update(todos)
            
            except IndexError:
                gui.Popup("Please select an item before pressing edit", font= ("Arial", 14))


        case "Complete":

            try:
                completed_todo= user_input_values["todo_show_list"][0]
                todos= Functions.get_todos()
                completed_index= todos.index(completed_todo)

                todos.pop(completed_index)
                Functions.write_todos(todos)
                todoprogram_window["todo_show_list"].update(todos)

            except IndexError:
                gui.Popup("Please select an item before pressing edit", font= ("Arial", 14))  

        case "todo_show_list":
            todoprogram_window["todo_item_add"].update(value=user_input_values["todo_show_list"][0])

        case gui.WIN_CLOSED:
            break

        case "Exit":
            break



todoprogram_window.close()

