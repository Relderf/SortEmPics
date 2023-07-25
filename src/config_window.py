import PySimpleGUI as sg
from tkinter.font import BOLD
import src.main_window as main_window
import src.helpers as helpers


sg.theme('DarkTanBlue')
PAD_TOP_S = (0,(20,0))
PAD_TOP_M = (0,(40,0))
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
LAYOUT_WIDTH = WINDOW_WIDTH - 40
DARKER_BACK = '#2d2d2d'


def load_layout():
    """ Provides the overall layout of the main window """
    config = helpers.load_config()
    input_folder = config['input_folder']
    output_folder = config['output_folder']
    layout = [[sg.Text('SortEmPics', font=('_', 30), justification='center')],
            [sg.Text('Config', font=('_', 24), justification='center', text_color="red")],
            [sg.Text('Select the source folder', font=('',10), justification='left', 
                     size=(40, 1), pad=PAD_TOP_M)],
            [
                sg.InputText(input_folder, font=('Trebuchet MS',14), size=(30,1), enable_events=True, key='-INPUT_FOLDER-'),
                sg.FolderBrowse()
            ],
            [sg.Text('Select the destination folder for the production', font=('',10), 
                     justification='left', size=(40, 1), pad=PAD_TOP_S)],
            [
                sg.InputText(output_folder, font=('Trebuchet MS',14), size=(30,1), enable_events=True, key='-OUTPUT_FOLDER-'),
                sg.FolderBrowse()
            ],
            [sg.Checkbox('Keep original files', key="-KEEP_ORIGINAL-", default=config["keep_original"], font=('Verdana',12), pad=PAD_TOP_M)],
            [sg.Checkbox('Create folder for sole file', key="-SINGLE_FILE_FOLDER-", default=config["single_file_folder"], font=('Verdana',12)),],
            [sg.Button('Save', size=(10,1), key='-SAVE-', font=('Verdana',16), pad=PAD_TOP_M)],
            [sg.Button('Back', size=(10,1), key='-BACK-', font=('Verdana',12), pad=PAD_TOP_S)]
    ]
    return sg.Window('SortEmPics', 
                     layout, margins=(20,40),
                     element_justification='c').finalize()


def main():
    """ Events loop method """
    window = load_layout()

    while True:
        event, values = window.read()
        if event == '-BACK-':
            window.close()
            main_window.main()
            break
        elif event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == '-SAVE-':
            helpers.update_config(values)
            window.close()
            main_window.main()
            break
    
    
if __name__ == '__main__':
    main()