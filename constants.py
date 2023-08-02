import os

CONFIG_PATH = os.getcwd() + os.sep + 'config.json'
BACKUP_PATH = "E:\\Programing\\SortEmPics playground\\backup\\"
DEV_IN_PATH = "E:\\Programing\\SortEmPics playground\\in\\"
DEV_OUT_PATH = "E:\\Programing\\SortEmPics playground\\out\\"
MONTHS = { 1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December" }
MONTHS_NUMS = { key: f"{key} - {MONTHS[key]}" for key in MONTHS.keys() }

PAD_Y = (0,(20,20))
PAD_TOP_S = (0,(20,0))
PAD_TOP_M = (0,(40,0))
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 400
LAYOUT_WIDTH = WINDOW_WIDTH - 40
DARKER_BACK = '#1e212b'