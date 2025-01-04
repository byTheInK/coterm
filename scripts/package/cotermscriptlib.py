import sys
from pathlib import Path
import os
import colorama

sys.path.append(str(Path(__file__).parent.parent.parent))

import bannerlib
import lib

class default:
    clear_with_banner: bool = True
    create_when_writing: bool = True
    line_per_page: int = 15
    banner_type: str = "family"
    complete_key: str = "tab"
    space_after_command: int = 0

class var:
    WINDOWS: bool = os.name == "nt"
    CLEAR_PREFIX: str = "cls"
    COTERM_DIR: str = lib.CURRENT

class color:
    class Foreground:
        RED: str = colorama.Fore.RED
        GREEN: str = colorama.Fore.GREEN
        YELLOW: str = colorama.Fore.YELLOW
        BLUE: str = colorama.Fore.BLUE
        MAGENTA: str = colorama.Fore.MAGENTA
        CYAN: str = colorama.Fore.CYAN
        WHITE: str = colorama.Fore.WHITE
        BLACK: str = colorama.Fore.BLACK
        RESET: str = colorama.Fore.RESET
    
    class Background:
        RED: str = colorama.Back.RED
        GREEN: str = colorama.Back.GREEN
        YELLOW: str = colorama.Back.YELLOW
        BLUE: str = colorama.Back.BLUE
        MAGENTA: str = colorama.Back.MAGENTA
        CYAN: str = colorama.Back.CYAN
        WHITE: str = colorama.Back.WHITE
        BLACK: str = colorama.Back.BLACK
        RESET: str = colorama.Back.RESET

class script:
    def banner(TYPE): bannerlib.BANNERS.print_banner_plus(TYPE)
    def clear(): os.system(var.CLEAR_PREFIX)

    def create_temporary_file(file_name: str):
        with open(f"{var.COTERM_DIR}\\script_temp\\{file_name}", "x"): pass
    
    def append_temporary_file(file_name: str, content: str):
        with open(f"{var.COTERM_DIR}\\script_temp\\{file_name}", "a") as file:
            file.write(content)
    
    def write_temporary_file(file_name: str, content: str):
        with open(f"{var.COTERM_DIR}\\script_temp\\{file_name}", "w") as file:
            file.write(content)
    
    def delete_temporary_file(file_name: str):
        os.remove(f"{var.COTERM_DIR}\\script_temp\\{file_name}")
    
    def read_temporary_file(file_name: str):
        with open(f"{var.COTERM_DIR}\\script_temp\\{file_name}", "r") as file:
            return file.read()

class Errors:
    Coterm404 = lib.CoTermErrors.CoTerm404
    CoTermPkgError = lib.CoTermErrors.CoTermPkgError
    CotermExtraError = lib.CoTermErrors.CotermExtraError
    CotermArgError = lib.CoTermErrors.CotermArgError

class printlib:
    cat = bannerlib.animallib.cat
    cow = bannerlib.animallib.cow
    dog = bannerlib.animallib.dog