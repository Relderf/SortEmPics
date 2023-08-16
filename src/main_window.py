import PySimpleGUI as sg
from tkinter.font import BOLD
import src.config_window as config_window
from src.sorter import sort_pictures
import constants as cts
import src.helpers as helpers

sg.theme('DarkTanBlue')


def load_layout():
    """ Provides the overall layout of the main window """
    layout = [
        [sg.Column([
            [sg.Text('SortEmPics', font=('_', 30), justification='center', background_color=cts.DARK_BACK_2, 
                     pad=(cts.PAD_Y), size=(12,1), text_color=cts.TEAL_400)],
            [sg.Button('Start Sorting', size=(14,1), key='-SORT-', 
                       font=('Verdana',16), pad=cts.PAD_TOP_S)],
            [sg.Button('Config', size=(14,1), key='-CONFIG-', 
                       font=('Verdana',16), pad=cts.PAD_Y)],
            [sg.Button('Exit', size=(14,1), key='-EXIT-', 
                       font=('Verdana',12), pad=cts.PAD_Y)]
        ], element_justification='center', background_color=cts.DARK_BACK_1,
        )],
        [sg.Text('Powered by Relderf - Etherground 2023', font=('', 9), justification='c')]
    ]
    return sg.Window('SortEmPics', 
                     layout, margins=(20,20),
                     element_justification='c').finalize()


def success_popup(sorted_amounts):
    sg.popup('Sorting completed! Found:'
        + '\nImages: ' + str(sorted_amounts["images"])
        + '\nVideos: ' + str(sorted_amounts["videos"])
        + '\nOther: ' + str(sorted_amounts["other"]),
        title='Items sorted', custom_text='Done'
    )


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
            if not helpers.load_config()['configured']:
                sg.popup('You need to configure the app first!', title='Error')
                continue
            sorted_amounts = sort_pictures()
            success_popup(sorted_amounts)
            
    
    
if __name__ == '__main__':
    main()