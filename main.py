import os
import cmd
import argparse
import shlex
import lib
from bannerlib import BANNERS
from subprocess import run as sbrun
from random import randint as random_number

WINDOWS: bool = os.name == "nt"
CLEAR_PREFIX: str = "cls" if WINDOWS else "clear"


#CUSTOMIZABLE
CLEAR_WITH_BANNER: bool = False # If enabled clears the screen completely
CREATE_WHEN_WRITING: bool = True # When enabled creates the file when writing if the file isn't there
LINE_PER_PAGE: int = 15
BANNER_TYPE: str = "family" # DO NOT PUT THE FILE EXTENSION
COMPLETE_KEY: str = "tab" # AUTO COMPLETE KEY

class coterm(cmd.Cmd):  
    prompt = "{}>> ".format(os.getcwd())

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
         super().__init__(completekey, stdin, stdout)
         BANNERS.print_banner_plus(BANNER_TYPE)

    def do_page(self, arg):
        try:
            with open(arg, "r") as file: 
                lib.general.pagerfirst(file.read(), LINE_PER_PAGE)
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            os.system(CLEAR_PREFIX)


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


    def do_append(self, arg):
        """Appends to a file."""
        if len(arg) < 2: 
            print("\n\n\n\tTHIS FUNCTION TAKES TWO ARGUMENTS!\n\n\n")
            return

        arg = shlex.split(arg)
        try:
            with open(arg[1], "a") as file: 
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

    def do_rm(self, arg):
        """Removes a file."""

        rm_parser = argparse.ArgumentParser(prog='rm')
        rm_parser.add_argument('-f', '--forced', action="store_true", help="Ends processes before trying to delete the file.")
        rm_parser.add_argument('file', help="Path to the file to delete.")
        
        try:
            args = rm_parser.parse_args(arg.split())
        except SystemExit: pass

        file_path = os.path.abspath(args.file)
        
        if args.forced:
            print(f"Force-deleting. Please wait until the program ends the processes.")
            lib.general.deattach_process(file_path)

        try:
            os.remove(file_path)
            print(f"File {file_path} removed successfully.")
        except FileNotFoundError:
            print(f"FILE NOT FOUND: {file_path}\nTip: You can create files with the 'mkf' command.")
        except Exception as e:
            print(f"ERROR: {e}")

    def do_echo(self, arg): print(arg)

    def do_srch(self, arg):
        if os.path.isfile(arg):
            print("{} exists and It is a file.".format(arg))
        elif os.path.isdir(arg):
            print("{} exists and It is a directory.".format(arg))
        else: print("{} doesn't exist.".format(arg))

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
            ls_parser.add_argument("-l", "--long", action="store_true", help="Ls but with bunch of details.")


            args = ls_parser.parse_args(arg.split())
            
            if args.count:
                print(len(items))
            elif args.long:
                print("\nPERMISSON  L O G     SIZE MODIFICATION ENTRY")
                lib.general.ls_long('.')
                print()
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
