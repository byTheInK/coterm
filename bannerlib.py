import os
from colorama import Fore as Foreground, init as coloroma_init
coloroma_init()

CLEAR_PREFIX: str = "clear"

class BANNERS:
    def get_options():
        prefix = os.path.dirname(os.path.abspath(__file__))
        new = os.listdir(f"{prefix}/banners")
        for index, value in enumerate(new):
            new[index] = value[:-4]
        return new
    
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
            BANNERS.print_banner(f"{prefix}/banners/{name}.txt")

class animallib:
     cow = r"""
           ^__^
           (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
                
                """
     
     dog = r"""
        / \__
        (   0\____
        /        Oo
        /   (_____/
        /_____/   
        
        """
     
     cat = r"""
         /\_/\  
        ( o.o ) 
         > ^ <
         
        """
