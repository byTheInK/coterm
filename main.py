import os
import cmd
import argparse
import shlex
from bannerlib import BANNERS
from subprocess import run as sbrun
from random import randint as random_number

WINDOWS: bool = os.name == "nt"
CLEAR_PREFIX: str = "cls" if WINDOWS else "clear"
CLEAR_WITH_BANNER: bool = False

#CUSTOMIZABLE
BANNER_TYPE: str = "family" # DO NOT PUT THE FILE EXTENSION
COMPLETE_KEY: str = "tab" # AUTO COMPLETE KEY

class coterm(cmd.Cmd):
    prompt = "{}>> ".format(os.getcwd())

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
         super().__init__(completekey, stdin, stdout)
         BANNERS.print_banner_plus(BANNER_TYPE)
    
    def do_mkdir(self, arg):
        """Creates a directory."""
        try:
            os.mkdir(arg)
        except FileExistsError as ERROR:
            print("FILE ALREADY EXISTS:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))
    
    def do_mkf(self, arg):
        """Creates a file."""
        try:
            with open(arg, "x"): pass
        except FileExistsError as ERROR:
            print("FILE ALREADY EXISTS:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    #############################
    #CAT CAT CAT CAT CAT CAT CAT#
    def do_cat(self, arg):
        try:
            with open(arg, "r") as file: 
                print(file.read())
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    
    def do_read(self, arg):
        try:
            with open(arg, "r") as file: 
                print(file.read())
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))
    #CAT CAT CAT CAT CAT CAT CAT#
    #############################

    def do_write(self, arg):
        """Writes to a file."""
        if len(arg) < 2: 
            print("\n\n\n\tTHIS FUNCTION TAKES TWO ARGUMENTS!\n\n\n")
            return

        arg = shlex.split(arg)
        try:
            with open(arg[1], "r+") as file: 
                file.write(arg[0])
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_write(self, arg):
        """
        Appends to a file.
        append "Hello, World!" test.txt
        """
        if len(arg) < 2: 
            print("\n\n\n\tTHIS FUNCTION TAKES TWO ARGUMENTS!\n\n\n")
            return

        arg = shlex.split(arg)
        try:
            with open(arg[1], "r+") as file: 
                file.write(arg[0])
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}\n Tip: You can create files with mkf command.".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))



    def do_cd(self, arg):
        """Changes the current directory."""
        try:
            os.chdir(arg)
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_ls(self, arg):
        """List the items in the current directory."""
        try:
            items = os.listdir(os.getcwd())
            
            ls_parser = argparse.ArgumentParser()
            ls_parser.add_argument("-c", "--count", action="store_true", help="Gives the count of items")

            args = ls_parser.parse_args(arg.split())
            
            if args.count:
                print(len(items))
            else:
                for index, item in enumerate(items):
                    print("[{}] = {}".format(index, item))

        except SystemExit: pass 
        
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    #############################
    #PWD PWD PWD PWD PWD PWD PWD#
    def do_dir(self, arg):
        """Prints put the current directory."""
        print("\n\n\n\tCURRENT DIRECTORY: {}\n\n\n".format(os.getcwd()))
    
    def do_cwd(self, arg):
        """Prints put the current directory."""
        print("\n\n\n\tCURRENT DIRECTORY: {}\n\n\n".format(os.getcwd()))

    def do_pwd(self, arg):
        """Prints put the current directory."""
        print("\n\n\n\tCURRENT DIRECTORY: {}\n\n\n".format(os.getcwd()))
    #PWD PWD PWD PWD PWD PWD PWD#
    #############################
    #---------------------------#
    #############################
    #CLR CLR CLR CLR CLR CLR CLR#
    def do_clr(self, arg):
        """Clears the screen."""
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(BANNER_TYPE) if not CLEAR_WITH_BANNER else None

    def do_clear(self, arg):
        """Clears the screen."""
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(BANNER_TYPE) if not CLEAR_WITH_BANNER else None

    def do_cls(self, arg):
        """Clears the screen."""
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(BANNER_TYPE) if not CLEAR_WITH_BANNER else None

    #CLR CLR CLR CLR CLR CLR CLR#   
    #############################

    def do_exit(self, arg):
        """Exits the command line interface."""
        os.system(CLEAR_PREFIX)
        return True

    def do_banner(self, arg):
        """Prints out the banner."""
        BANNERS.print_banner_plus(BANNER_TYPE)
    
    def do_getopts(self, arg):
        """
        Gives options about a topic.
        Options:
            - banner (Prints all of the usable banners. If you want your own banner check out the guide in https://github.com/byTheInK/coterm.)
        """
        if arg.lower() == "banner":
            print(BANNERS.get_options(), "Don't put .txt in the settings.")
        else:
            print("\n\n\n\tNEEDS AN VALID OPTION TYPE. TYPE \"help getopts\".\n\n\n")
    
    def do_sys(self, arg):
        """
        Uses your terminal to execute commands.
        sys nano test.txt
        """
        try:
            if WINDOWS:
                arg = shlex.split(arg)
                sbrun(arg, shell=True)
            else:
                os.system(arg)

        except Exception as ERROR:
            print("\n{}".format(ERROR))

    def do_random(self, arg):
        """Gives a random number between two numbers."""
        arg = arg.split()

        if len(arg) < 2:
            print("\n\n\n\tTHIS FUNCTION TAKES TWO ARGUMENTS!\n\n\n")
            return
        try:
            print("\n\n\n\t{}\n\n\n".format(random_number(int(arg[0]), int(arg[1]))))
        except Exception as ERROR:
            print("ERROR:\n{} Please put integers if you didn't.".format(ERROR))


    def postcmd(self, stop, line):
        """Update the prompt after every command."""
        self.prompt = "{}>> ".format(os.getcwd())
        return stop



if __name__ == "__main__":  
     coterm(COMPLETE_KEY).cmdloop()
