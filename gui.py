import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
add_btn = sg.Button("Add")
input_box = sg.InputText(tooltip = "Enter todo")
window = sg.Window('My app',layout=[[label],[input_box,add_btn]])
window.read()
print("hello")
window.close()