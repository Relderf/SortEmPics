import PySimpleGUI as sg
from tkinter.font import BOLD
import src.main_window as main_window
import src.helpers as helpers
import constants as cts


def load_layout():
    """ Provides the overall layout of the config window """
    config = helpers.load_config()
    input_folder = config['input_folder']
    output_folder = config['output_folder']
    layout = [
        [sg.Text('SEP Config', font=('', 28), justification='center', size=(12,1),
                 text_color=cts.TEAL_400, background_color=cts.DARK_BACK_2)],
        [sg.Column([
            *browsers_layout(input_folder, output_folder),
            [sg.Text('_' * cts.SEP_LENGHT, text_color='gray', pad=cts.PAD_BOT_XS)],
            *checkboxes_layout(config),
            [sg.Text('_' * cts.SEP_LENGHT, text_color='gray', pad=cts.PAD_BOT_XS)],
            *folder_naming_layout(config),
        ], element_justification='center', size=(345,300),
                   scrollable=True, vertical_scroll_only=True)],
            [
                sg.Button('Save', size=(10,1), key='-SAVE-', font=('Verdana',16), pad=(20,20)),
                sg.Button('Back', size=(10,1), key='-BACK-', font=('Verdana',16), pad=(20,20))
            ],
        [sg.Text('Powered by Relderf - Etherground 2023', font=('', 9), justification='c',
                 background_color=cts.DARK_BACK_1)]
    ]
    return sg.Window('SortEmPics', 
                     layout, margins=(20,20), background_color=cts.DARK_BACK_1, 
                     element_justification='c').finalize()

def folder_naming_layout(config):
    return (
        [sg.Text('Select the naming format for month folders.', 
                    font=('',12, 'italic'), justification='left', 
            size=(36, 1), text_color=cts.TEAL_200)],
        [sg.Radio("Number and name", "number_name", key="-NUMBER_AND_NAME-", 
                    default=config["month_folder_format"]=="number_name", font=('Verdana',12))],
        [sg.Radio("Number only", "number_name", key="-NUMBER_ONLY-", 
                    default=config["month_folder_format"]=="number_only", font=('Verdana',12))],
        [sg.Radio("Name only", "number_name", key="-NAME_ONLY-", 
                    default=config["month_folder_format"]=="name_only", font=('Verdana',12),
                    pad=cts.PAD_BOT_XS)]
    )

def checkboxes_layout(config):
    return(
        [sg.Checkbox('Keep original files', key="-KEEP_ORIGINAL-", 
                        default=config["keep_original"], font=('Verdana',12))],
        [sg.Text("Select whether 'day' folders with only 1 file are created (checked), "
                    + "or those files are placed in the parent month folder:", 
                    font=('',12, 'italic'), justification='left', size=(36, 3), 
                    text_color=cts.TEAL_200)],
        [sg.Checkbox('Create sole file folders', key="-SINGLE_FILE_FOLDER-", 
                        default=config["single_file_folder"], font=('Verdana',12))],
        [sg.Text("Checking the option below will create two separate root folders completly "
                    + "separate one from another, one for images and one for videos. Otherwise, "
                    + "they are put together in the same day folders", 
                    font=('',12, 'italic'), justification='left', size=(36, 5), 
                    text_color=cts.TEAL_200)],
        [sg.Checkbox('Images and Videos separated', key="-IMAGES_VIDEOS_SEPARATE-", 
                        default=config["images_videos_separate"], font=('Verdana',12))],
    )
    
def browsers_layout(input_folder, output_folder):
    return (
        [sg.Text('Select the source folder where your pics are.', font=('',12, 'italic'), justification='left', 
                size=(36, 1), text_color=cts.TEAL_200, pad=cts.PAD_TOP_XS)],
        [
            sg.InputText(input_folder, font=('Trebuchet MS',12), size=(32,1), enable_events=True, key='-INPUT_FOLDER-'),
            sg.FolderBrowse()
        ],
        [sg.Text('Select the destination folder for the production.', font=('',12, 'italic'), 
            justification='left', size=(36, 1), pad=cts.PAD_TOP_S, text_color=cts.TEAL_200)],
        [
            sg.InputText(output_folder, font=('Trebuchet MS',12), size=(32,1), enable_events=True, key='-OUTPUT_FOLDER-'),
            sg.FolderBrowse()
        ]
    )

def main():
    """ Events loop method for the config window """
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