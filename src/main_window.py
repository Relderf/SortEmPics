import PySimpleGUI as sg
from tkinter.font import BOLD
import src.config_window as config_window
from src.sorter import sort_pictures
import constants as cts


sg.theme('DarkTanBlue')



def load_layout():
    """ Provides the overall layout of the main window """
    layout = [
        [sg.Column([
            [sg.Text('SortEmPics', font=('_', 30), justification='center', pad=cts.PAD_Y)],
            [sg.Button('Start Sorting', size=(14,1), key='-SORT-', font=('Verdana',16), pad=cts.PAD_TOP)],
            [sg.Button('Config', size=(14,1), key='-CONFIG-', font=('Verdana',16), pad=cts.PAD_Y)],
            [sg.Button('Exit', size=(14,1), key='-EXIT-', font=('Verdana',12), pad=cts.PAD_Y)]
        ], element_justification='center', background_color=cts.DARKER_BACK)]
    ]
    return sg.Window('SortEmPics', 
                     layout, margins=(50,10),
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