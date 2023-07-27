import os
import json
import constants as cts
import shutil

def preset():
    """ Create the config file if it doesn't exist """
    if not os.path.exists(f"{cts.CONFIG_PATH}"):
        data = {
            "input_folder": "C:/",
            "output_folder": "C:/sortedPics/",
            "keep_original": True,
            "single_file_folder": False,
            "month_folder_format": "number_name"
        }
        with open(f"{cts.CONFIG_PATH}", "w", encoding = "utf-8") as config:
            json.dump(config, data, indent = 4, ensure_ascii = False)

def load_config():
    """ Load the config file and return the data """
    with open(f"{cts.CONFIG_PATH}", "r", encoding = "utf-8") as json_file:
        config = json.load(json_file)
    return config

def save_config(config):
    """ Save the config file with the new data """
    with open(f"{cts.CONFIG_PATH}", "w", encoding = "utf-8") as config_file:
        json.dump(config, config_file, indent = 4, ensure_ascii = False)
        
def copy_test_files():
    """ Copy the test files to the dev_in folder """
    items = os.listdir(cts.DEV_IN_PATH)
    backup_file = os.listdir(cts.BACKUP_PATH)
    if len(items) < len(backup_file):
        for file in backup_file:
            if file not in items:
                shutil.copy(f"{cts.BACKUP_PATH}{file}", cts.DEV_IN_PATH)

def update_config(values):
    print(values)
    config = load_config()
    in_path = values.get('-INPUT_FOLDER-')
    out_path = values.get('-OUTPUT_FOLDER-')
    config["input_folder"] = in_path + "/" if in_path[-1] != "/" else in_path
    config["output_folder"] = out_path + "/" if out_path[-1] != "/" else out_path
    config["keep_original"] = values.get('-KEEP_ORIGINAL-')
    config["single_file_folder"] = values.get('-SINGLE_FILE_FOLDER-')
    config["month_folder_format"] = ("number_name" if values.get('-NUMBER_AND_NAME-') 
        else "number_only" if values.get('-NUMBER_ONLY-') 
        else "name_only")
    save_config(config)