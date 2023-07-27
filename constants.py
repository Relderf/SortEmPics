import os

CONFIG_PATH = os.getcwd() + os.sep + 'config.json'
BACKUP_PATH = "E:\\Programing\\SortEmPics playground\\backup\\"
DEV_IN_PATH = "E:\\Programing\\SortEmPics playground\\in\\"
DEV_OUT_PATH = "E:\\Programing\\SortEmPics playground\\out\\"
MONTHS = { 1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December" }
MONTHS_NUMS = { key: f"{key} - {MONTHS[key]}" for key in MONTHS.keys() }