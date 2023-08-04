import os

CONFIG_PATH = os.getcwd() + os.sep + 'config.json'
BACKUP_PATH = "E:\\Programing\\SortEmPics playground\\backup\\"
DEV_IN_PATH = "E:\\Programing\\SortEmPics playground\\in\\"
DEV_OUT_PATH = "E:\\Programing\\SortEmPics playground\\out\\"
MONTHS = { 1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December", "unknown": "Unknown" }
MONTHS_NUMS = { key: f"{key} - {MONTHS[key]}" for key in MONTHS.keys() }

PAD_Y = (0,(20,20))
PAD_TOP_XS = (0,(10,0))
PAD_TOP_S = (0,(20,0))
PAD_TOP_M = (0,(40,0))
PAD_BOT_XS = (0,(0,10))
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 450
LAYOUT_WIDTH = WINDOW_WIDTH - 40
DARK_BACK_1 = '#1e212b'
DARK_BACK_2 = "#1b1d26"
SEP_LENGHT = 40
TEAL_100 = "#d1fae5"
TEAL_200 = "#a7f3d0"
TEAL_300 = "#6ee7b7"
TEAL_400 = "#34d399"
TEAL_500 = "#10b981"
TEAL_600 = "#059669"
TEAL_700 = "#047857"
TEAL_800 = "#065f46"