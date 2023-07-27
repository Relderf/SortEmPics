from src.helpers import load_config
import constants as cts
import os
from datetime import datetime
from PIL import Image, ExifTags


def sort_pictures():
    config = load_config()
    in_folder_path = config['input_folder']
    source_items = os.listdir(config['input_folder'])
    for item in source_items:
        path = in_folder_path + "/" + item
        metadata = get_file_details(path)
        secure_folder(out_path = config['output_folder'],
                      year = metadata['year'],
                      month = cts.MONTHS[metadata['month']]
                      )


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
    
        
    