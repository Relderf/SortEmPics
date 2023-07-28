from src.helpers import load_config
import constants as cts
import os
from datetime import datetime
from PIL import Image, ExifTags


def sort_pictures():
    config = load_config()
    in_folder_path = config['input_folder']
    source_items = os.listdir(config['input_folder'])
    if config["single_file_folder"]:
        quantities = get_quantities(in_folder_path, source_items)
    for item in source_items:
        input_file_path = in_folder_path + item
        metadata = get_file_details(input_file_path)
        
        output_folder = config['output_folder']
        year_folder = metadata['year']
        month_folder = format_month(config, metadata['month'])
        secure_folder(output_folder, year_folder, month_folder)
        move_file(input_file_path, output_folder, year_folder, month_folder, metadata['name'])


def get_file_details(file):
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
    return {}


def secure_folder(out_path, year, month):
    if not os.path.exists(f"{out_path}/{year}"):
        os.mkdir(f"{out_path}/{year}")
    if not os.path.exists(f"{out_path}/{year}/{month}"):
        os.mkdir(f"{out_path}/{year}/{month}")


def move_file(in_path, out_path, year, month, name):
    os.rename(in_path, output_filename(out_path, year, month, name))
    
    
def output_filename(out_path, year, month, name):
    return f"{out_path}{year}/{month}/{name}"


def get_quantities(in_folder_path, source_items):
    quantities = {}
    for item in source_items:
        metadata = get_file_details(in_folder_path + item)
        if metadata['year'] in quantities:
            if metadata['month'] in quantities[metadata['year']]:
                quantities[metadata['year']][metadata['month']] += 1
            else:
                quantities[metadata['year']][metadata['month']] = 1
        else:
            quantities[metadata['year']] = { metadata['month']: 1 }
    return quantities
    
def format_month(config, month_number):
    name_format = config["month_folder_format"]
    if name_format == "number":
        return month_number
    if name_format == "name":
        return cts.MONTHS[month_number]
    if name_format == "number_name":
        return f"{month_number} - {cts.MONTHS[month_number]}"