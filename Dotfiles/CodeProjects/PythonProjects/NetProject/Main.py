import PySimpleGUI as sg

layout = [ [sg.Button()],
           [sg.Input()], [sg.Button(key="-1-")],
           [sg.Button()],[sg.Text("Esta es una prueba")],
           [sg.Button()]
           ]

win = sg.Window("Demo", layout)
r = win.read()
print(r)