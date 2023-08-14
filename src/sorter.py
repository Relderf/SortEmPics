from src.helpers import load_config
import constants as cts
import os
from datetime import datetime
from PIL import Image, ExifTags
import shutil
from filecmp import cmp


def sort_pictures():
    """ Sorts the pictures in the input folder 
    into the output folder, according to
    the user configuration """
    config = load_config()
    in_folder_path = config['input_folder']
    source_items = []
    scan_files(in_folder_path, source_items)
    
    if not config["single_file_folder"]:
        quantities = get_quantities(source_items)
    else:
        quantities = None
    
    for item in source_items:
        print(item)
        metadata = get_file_details(item)
        print(metadata)
        
        output_folder = config['output_folder']
        year_folder = metadata['year']
        month_folder = format_month(config, metadata['month'])
        day_folder = metadata['day']
        if not config["single_file_folder"] and quantities[year_folder][metadata['month']][day_folder]["quantity"] < 2:
            day_folder = None
        secure_folder(output_folder, year_folder, month_folder, day_folder)
        move_opt = not config["keep_original"]
        organize_file(move_opt, item, output_folder, year_folder, month_folder, day_folder, metadata['name'])


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


def organize_file(move, in_path, out_base, year, month, day, name):
    """ Decide if the file should be created at destination or not """
    out_path = (f"{out_base}{year}/{month}/{day}/{name}" 
                if day != None 
                else f"{out_base}{year}/{month}/{name}")
    if not os.path.exists(out_path):
        move_file(move, in_path, out_path)
    elif not cmp(in_path, out_path):
        move_file(move, in_path, rename_file(out_path))
    elif move:
        os.remove(in_path)


def move_file(move, in_path, out_path):
    """ Move or copy a given file to the output folder """
    if move:
        os.rename(in_path, out_path)
    else:
        shutil.copy(in_path, out_path)


def rename_file(out_path):
    """ Returns a new name for the file if it already exists """
    name, ext = os.path.splitext(out_path)
    i = 2
    while os.path.exists(out_path):
        out_path = f"{name} ({i}){ext}"
        i += 1
    return out_path


def get_quantities(source_items):
    """ Returns a dictionary with the quantities of files
    to determine if the day folder should be created"""
    quantities = {}
    for item in source_items:
        data = get_file_details(item)
        quantities.setdefault(data['year'], {}).setdefault(data['month'], {}).setdefault(data['day'], {}).setdefault('quantity', 0)
        quantities[data['year']][data['month']][data['day']]['quantity'] += 1
        if quantities[data['year']][data['month']][data['day']]['quantity'] == 1:
            quantities[data['year']][data['month']][data['day']]['file'] = data['path']
        elif cmp(quantities[data['year']][data['month']][data['day']]['file'], data['path']):
            quantities[data['year']][data['month']][data['day']]['quantity'] -= 1
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


def scan_files(folder, files):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item).replace("\\", "/")
        if os.path.isdir(item_path):
            scan_files(item_path, files)
        else:
            files.append(item_path)

