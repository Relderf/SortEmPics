import PySimpleGUI as sg
from tkinter.font import BOLD
import os


sg.theme('DarkTanBlue')
HEADER_IMG = os.getcwd() + os.sep + 'img' + os.sep + 'Mempy principal.png'


def load_layout():

    layout = [[sg.Text('SortEmPics', font=('_', 30), justification='center', pad=(20,0))],
            [sg.Text('Select the source folder', font=('',10))],
            [sg.Button('...', font=('Trebuchet MS',14), size=(16,1), key='jugar')],
            [sg.InputText('C:\\', font=('Trebuchet MS',14), size=(40,1), key='folder', pad=(20,0))],
            [sg.Text('Select the destination folder for the production', font=('',10))],
            [sg.Button('...', font=('Trebuchet MS',14), size=(16,1), key='target')],
            [sg.InputText('C:\\sortedPics', font=('Trebuchet MS',14), size=(40,1), key='folder', pad=(20,0))],
            [sg.Button('Start Sorting', key='sort', font=('Verdana',12), pad=(20,0))],
            [sg.Button('Exit', size=(5,1), key='exit', font=('Verdana',12))]
    ]
    return sg.Window('SortEmPics', 
                     layout, margins=(30,30),
                     element_justification='c').finalize()


def main():
    window = load_layout()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'salir':
            break
    window.close()
    
    
if __name__ == '__main__':
    main()