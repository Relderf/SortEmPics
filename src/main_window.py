import PySimpleGUI as sg
from tkinter.font import BOLD
import src.config_window as config_window
from src.sorter import sort_pictures


sg.theme('DarkTanBlue')
PAD_TOP = (0,(20,0))
PAD_TOP_M = (0,(40,0))
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
LAYOUT_WIDTH = WINDOW_WIDTH - 40
DARKER_BACK = '#2d2d2d'


def load_layout():
    """ Provides the overall layout of the main window """
    layout = [[sg.Text('SortEmPics', font=('_', 30), justification='center')],
            [sg.Button('Start Sorting', key='-SORT-', font=('Verdana',16), pad=PAD_TOP_M)],
            [sg.Button('Config', key='-CONFIG-', font=('Verdana',16), pad=PAD_TOP_M)],
            [sg.Button('Exit', size=(5,1), key='-EXIT-', font=('Verdana',12), pad=PAD_TOP)]
    ]
    return sg.Window('SortEmPics', 
                     layout, size=(WINDOW_WIDTH, WINDOW_HEIGHT), margins=(20,40),
                     element_justification='c').finalize()


def main():
    """ Events loop method """
    window = load_layout()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break
        elif event == '-CONFIG-':
            window.close()
            config_window.main()
            break
        if event == '-SORT-':
            sort_pictures()
    
    
if __name__ == '__main__':
    main()