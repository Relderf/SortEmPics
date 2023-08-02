from src import main_window as mw
from src.helpers import copy_test_files, preset


def main():
    preset()
    copy_test_files()
    mw.main()
    
if __name__ == '__main__':
    main()