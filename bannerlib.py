import os
from color.color.colorama import Fore as Foreground, init as coloroma_init
coloroma_init()

WINDOWS: bool = os.name == "nt"
CLEAR_PREFIX: str = "cls" if WINDOWS else "clear"

class BANNERS:
    def get_options():
        prefix = os.path.dirname(os.path.abspath(__file__))
        return os.listdir(f"{prefix}\\banners") if WINDOWS else f"{prefix}/banners"
    
    def print_banner(file: str):
        os.system(CLEAR_PREFIX)
        try:
            with open(file, "r") as text:
                print(Foreground.GREEN+text.read())
        
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND ERROR:\n{}".format(ERROR))
            return

    def print_banner_plus(name: str):
            prefix = os.path.dirname(os.path.abspath(__file__))
            BANNERS.print_banner(f"{prefix}\\banners\\{name}.txt" if WINDOWS else f"{prefix}/banners/{name}.txt")