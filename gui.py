import time

import functions
import FreeSimpleGUI as sg

sg.theme("DarkPurple4")
clock = sg.Text('',key = 'clock')
label = sg.Text("Type in a todo")
add_btn = sg.Button("Add")
input_box = sg.InputText(tooltip = "Enter todo",key = "todo")
list_box = sg.Listbox(values=functions.get_todos(), key ='todos',
                      enable_events= True, size = [45,10])
exit_label = sg.Button("Exit")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

# btn_labels = ["Close","Apply"]
# layout = []
# for bl in btn_labels:
#     layout.append([sg.Button(bl)])
layout = [[clock],
          [label],
          [input_box,add_btn],
          [list_box,edit_button,complete_button],
          [exit_label]]
window = sg.Window('My app',
                   layout= layout,
                   font = ('Helvetica',20))

while True:

    event, values = window.read(timeout = 500)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))

    print(1,event)
    print(2,values)
    print(3,values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
            sg.popup("success!")
            window['todos'].update(values = todos)


        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                print(todos)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                sg.popup("please select a task")

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                sg.popup("Please select a task")




        case 'todos':
            window['todo'].update(value = values['todos'][0])
        case "Exit":
            break
sg.popup("Bye")
window.close()