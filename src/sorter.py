from src.helpers import load_config
import os
from datetime import datetime
from PIL import Image, ExifTags
import json


def sort_pictures():
    config = load_config()
    in_folder_path = config['input_folder']
    source_items = os.listdir(config['input_folder'])
    for item in source_items:
        print(get_file_details(in_folder_path + item))


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
        
    