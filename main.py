import os
import cmd
import argparse
from subprocess import run as sbrun

from color.color.colorama import Fore as Foreground, init as coloroma_init
coloroma_init()
WINDOWS: bool = os.name == "nt"
CLEAR_PREFIX: str = "cls" if WINDOWS else "clear"
CLEAR_WITH_BANNER: bool = False

#CUSTOMIZABLE
BANNER_TYPE: str = "family" # DO NOT PUT THE FILE EXTENSION
COMPLETE_KEY: str = "tab" # AUTO COMPLETE KEY

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


class coterm(cmd.Cmd):
    prompt = "{}>> ".format(os.getcwd())
    def __init__(self, completekey = "tab", stdin = None, stdout = None):
         super().__init__(completekey, stdin, stdout)
         BANNERS.print_banner_plus(BANNER_TYPE)
    
    def do_cd(self, arg):
        """Changes the current directory."""
        try:
            os.chdir(arg)
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_ls(self, arg):
        """List the items in the current directory with an optional count."""
        items = os.listdir(os.getcwd())
        
        ls_parser = argparse.ArgumentParser()
        ls_parser.add_argument("-c", "--count", action="store_true", help="Gives the count of items")

        args = ls_parser.parse_args(arg.split())
        
        if args.count:
            print(len(items))
        else:
            for index, item in enumerate(items):
                print("[{}] = {}".format(index, item))

    #############################
    #PWD PWD PWD PWD PWD PWD PWD#
    def do_dir(self, arg):
        print("\n\n\n\tCURRENT DIRECTORY: {}\n\n\n".format(os.getcwd()))
    
    def do_cwd(self, arg):
        print("\n\n\n\tCURRENT DIRECTORY: {}\n\n\n".format(os.getcwd()))

    def do_pwd(self, arg):
        print("\n\n\n\tCURRENT DIRECTORY: {}\n\n\n".format(os.getcwd()))
    #PWD PWD PWD PWD PWD PWD PWD#
    #############################
    #---------------------------#
    #############################
    #CLR CLR CLR CLR CLR CLR CLR#
    def do_clr(self, arg):
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(BANNER_TYPE) if not CLEAR_WITH_BANNER else None

    def do_clear(self, arg):
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(BANNER_TYPE) if not CLEAR_WITH_BANNER else None

    def do_cls(self, arg):
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(BANNER_TYPE) if not CLEAR_WITH_BANNER else None

    #CLR CLR CLR CLR CLR CLR CLR#   
    #############################

    def do_exit(self, arg):
        os.system(CLEAR_PREFIX)
        return True

    def do_banner(self, arg):
        BANNERS.print_banner_plus(BANNER_TYPE)
    
    def do_getopts(self, arg):
        """
        Options:
            - banner (Prints all of the usable banners. If you want your own banner check out the guide in https://github.com/byTheInK/coterm.)
        """
        if arg.lower() == "banner":
            print(BANNERS.get_options(), "Don't put .txt in the settings.")
        else:
            print("\n\n\n\tNEEDS AN VALID OPTION TYPE. TYPE \"help getopts\".\n\n\n")
    
    def do_sys(self, arg):
        if WINDOWS:
            arg = arg.split(" ")
            sbrun(arg, shell=True)
        else:
            os.system(arg)

    def postcmd(self, stop, line):
        """Update the prompt after every command."""
        self.prompt = "{}>> ".format(os.getcwd())
        return stop



if __name__ == "__main__":  
     coterm(COMPLETE_KEY).cmdloop()
