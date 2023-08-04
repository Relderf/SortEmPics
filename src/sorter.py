from src.helpers import load_config
import constants as cts
import os
from datetime import datetime
from PIL import Image, ExifTags
import shutil


def sort_pictures():
    """ Sorts the pictures in the input folder 
    into the output folder, according to
    the user configuration """
    config = load_config()
    in_folder_path = config['input_folder']
    source_items = os.listdir(config['input_folder'])
    if not config["single_file_folder"]:
        quantities = get_quantities(in_folder_path, source_items)
    else:
        quantities = None
    
    for item in source_items:
        input_file_path = in_folder_path + item
        metadata = get_file_details(input_file_path)
        
        output_folder = config['output_folder']
        year_folder = metadata['year']
        month_folder = format_month(config, metadata['month'])
        day_folder = metadata['day']
        if not config["single_file_folder"] and quantities[year_folder][metadata['month']][day_folder] < 2:
            day_folder = None
        secure_folder(output_folder, year_folder, month_folder, day_folder)
        move_opt = not config["keep_original"]
        move_file(move_opt, input_file_path, output_folder, year_folder, month_folder, day_folder, metadata['name'])


def get_file_details(file):
    """ Returns a dictionary with the 
    file metadata details """
    image_exif = Image.open(file)._getexif()
    if image_exif:
        exif = { ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS and type(v) is not bytes }
        date_obj = datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
        return {
            'name': os.path.basename(file),
            'path': os.path.dirname(file) + "/" + os.path.basename(file),
            'year': date_obj.year,
            'month': date_obj.month,
            'day': date_obj.day,
            'hour': date_obj.hour,
            'minute': date_obj.minute,
            'second': date_obj.second
        }
    return {
        'year': 'unknown', 
        'month': 'unknown', 
        'day': 'unknown', 
        'name': os.path.basename(file)
    }


def secure_folder(out_path, year, month, day):
    """ Makes sure the output folder exists """
    if not os.path.exists(f"{out_path}/{year}"):
        os.mkdir(f"{out_path}/{year}")
    if not os.path.exists(f"{out_path}/{year}/{month}"):
        os.mkdir(f"{out_path}/{year}/{month}")
    if day != None and not os.path.exists(f"{out_path}/{year}/{month}/{day}"):
        os.mkdir(f"{out_path}/{year}/{month}/{day}")


def move_file(move, in_path, out_base, year, month, day, name):
    """ Move or copy a given file to the output folder """
    out_path = (f"{out_base}{year}/{month}/{day}/{name}" 
                if day != None 
                else f"{out_base}{year}/{month}/{name}")
    if move:
        os.rename(in_path, out_path)
    else:
        shutil.copy(in_path, out_path)


def get_quantities(in_folder_path, source_items):
    """ Returns a dictionary with the quantities of files
    to determine if the day folder should be created"""
    quantities = {}
    for item in source_items:
        metadata = get_file_details(in_folder_path + item)
        quantities.setdefault(metadata['year'], {}).setdefault(metadata['month'], {}).setdefault(metadata['day'], 0)
        quantities[metadata['year']][metadata['month']][metadata['day']] += 1
    return quantities


def format_month(config, month_number):
    """ Returns the proper month folder name
    according to the user configuration """
    name_format = config["month_folder_format"]
    if name_format == "number":
        return month_number
    if name_format == "name":
        return cts.MONTHS[month_number]
    if name_format == "number_name":
        return f"{month_number} - {cts.MONTHS[month_number]}"
    