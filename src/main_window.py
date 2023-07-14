import PySimpleGUI as sg
from tkinter.font import BOLD
import os


sg.theme('DarkTanBlue')
HEADER_IMG = os.getcwd() + os.sep + 'img' + os.sep + 'Mempy principal.png'
PAD_TOP = (0,(20,0))
PAD_TOP_M = (0,(40,0))
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
LAYOUT_WIDTH = WINDOW_WIDTH - 40

def load_layout():
    

    layout = [[sg.Text('SortEmPics', font=('_', 30), justification='center')],
            [sg.Text('Select the source folder', font=('',10), justification='left', 
                     size=(40, 1), pad=PAD_TOP_M)],
            [
                sg.InputText('C:\\', font=('Trebuchet MS',14), size=(30,1), key='folder'),
                sg.Button('...', font=('Trebuchet MS',10), size=(5,1), key='jugar')
            ],
            [sg.Text('Select the destination folder for the production', font=('',10), 
                     justification='left', size=(40, 1), pad=PAD_TOP)],
            [
                sg.InputText('C:\\sortedPics', font=('Trebuchet MS',14), size=(30,1), key='folder'),
                sg.Button('...', font=('Trebuchet MS',10), size=(5,1), key='target'),
            ],
            [sg.Button('Start Sorting', key='sort', font=('Verdana',16), pad=PAD_TOP_M)],
            [sg.Button('Exit', size=(5,1), key='exit', font=('Verdana',12), pad=PAD_TOP)]
    ]
    return sg.Window('SortEmPics', 
                     layout, margins=(20,40),
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