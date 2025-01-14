import os
import cmd
import argparse
from bannerlib import animallib
import lang
import shlex
import lib
from distro import name as linux_distribution
from getpass import getuser
import requests
import shutil
from bannerlib import BANNERS
import zipfile
import tarfile
import paramiko
from pathlib import Path
import psutil
from pythonping import ping
import wget
from random import randint as random_number

Clipboard: str = ""
CLEAR_PREFIX: str = "clear"
CURRENT: str = os.path.dirname(os.path.abspath(__file__))

#CUSTOMIZABLE
clear_with_banner: bool = True
create_when_writing: bool = True
line_per_page: int = 15
banner_type: str = "family"
complete_key: str = "tab"
space_after_command: int = 0

class coterm(cmd.Cmd):  
    prompt = "{}>> ".format(os.getcwd())

    def __init__(self, stdin=None, stdout=None):
        super().__init__(stdin=stdin, stdout=stdout)
        global clear_with_banner
        global create_when_writing
        global line_per_page
        global banner_type
        global complete_key
        global space_after_command

        config_dict = lib.config.initialize_config()

        clear_with_banner = bool(config_dict.get("CLEAR_WITH_BANNER", clear_with_banner))
        create_when_writing = bool(config_dict.get("CREATE_WHEN_WRITING", create_when_writing))
        line_per_page = int(config_dict.get("LINE_PER_PAGE", line_per_page))
        banner_type = config_dict.get("BANNER_TYPE", banner_type)
        complete_key = config_dict.get("COMPLETE_KEY", complete_key)
        space_after_command = int(config_dict.get("SPACE_AFTER_COMMAND", space_after_command))

        print(banner_type)
        BANNERS.print_banner_plus(banner_type)

    def do_opencwd(self, arg):
        """Open current working directory."""
        os.system("dolphin .")

    def do_chown(self, arg):
        """
        Changes the owner and the group of a file.
        chown test.txt <userid> <groupid>
        """

        arg = shlex.split(arg)
        chown_parser = argparse.ArgumentParser()
        chown_parser.add_argument("-r", "--recursive", action="store_true", help="Changes the owner and the group of a file recursively.")
        opts, args = chown_parser.parse_known_args(arg)

        if len(args) < 3:
            print("THIS FUNCTION TAKES THREE ARGUMENTS!")
            return

        file_path, user_id, group_id = args[0], args[1], args[2]

        if opts.recursive:
            try:
                for root, dirs, files in os.walk(file_path):
                    for name in dirs:
                        shutil.chown(os.path.join(root, name), user=user_id, group=group_id)
                    for name in files:
                        shutil.chown(os.path.join(root, name), user=user_id, group=group_id)
                print("\nChanged the owner and the group recursively.")
            except FileNotFoundError as ERROR:
                print("FILE NOT FOUND:\n{}".format(ERROR))
            except Exception as ERROR:
                print("ERROR:\n{}".format(ERROR))
            return

        try:
            shutil.chown(file_path, user=user_id, group=group_id)
            print("\nChanged the owner and the group.")
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_run(self, arg):
        """Runs a script"""
        arg = shlex.split(arg)

        if len(arg) < 2:
            arg.append("")

        if not arg[0].endswith(".py"):
            arg[0] += ".py"

        _conf_list = {
            "prompt": self.prompt,
            "clear_with_banner": clear_with_banner,
            "create_when_writing":create_when_writing,
            "banner_type": banner_type,
            "space_after_command": space_after_command,
            "line_per_page":line_per_page,
            "complete_key": complete_key}

        lang.main(f"{CURRENT}/scripts/{arg[0]}", arg[1:], _conf_list)

    def do_mkscript(self, arg):
        """Creates a script."""
        try:
            if arg[-3:] != ".py": arg += ".py"
            with open(f"{CURRENT}/scripts/{arg}", "x"): pass
            print("Created file {} sucsessfully.".format(arg))
        except FileExistsError as ERROR:
            print("FILE ALREADY EXISTS:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))
    
    def do_openscript(self, arg):
        """Creates a script."""
        try:
            if arg[-3:] != ".py": arg += ".py"

            if not os.path.exists(f"{CURRENT}/scripts/{arg}"): raise FileNotFoundError("{} not found".format(arg)); return
            if not os.path.isfile(f"{CURRENT}/scripts/{arg}"): raise FileNotFoundError("{} is not a file".format(arg)); return

            os.system(f"vim {CURRENT}/scripts/{arg}")
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))


    def do_ip(self, arg): lib.general.ip()

    def do_rqs(self, arg):
        """A request command. It is like curl in bash."""
        rqs_parser = argparse.ArgumentParser()
        rqs_parser.add_argument("-u", "--url", help="URL to send the request.")
        rqs_parser.add_argument("-o", "--output", help="Output file to save the response.")
        rqs_parser.add_argument("-m", "--method", help="HTTP method to use.")

        args = rqs_parser.parse_args(shlex.split(arg))
        
        try:
            response = requests.get(args.url) if not args.method else requests.request(args.method, args.url)
            if args.output:
                with open(args.output, "w") as file:
                    file.write(response.text)
            else:
                print(response.text)
        except Exception as ERROR:
            print(f"ERROR:\n{ERROR}")


    def do_memory(self, arg):
        """Gives memory information."""
        try:
            lib.general.memory()
        except Exception as ERROR:
            print(f"ERROR:\n{ERROR}")

    def do_arczip(self, arg):
        """Compresses to zip."""
        arg = shlex.split(arg)
        if len(arg) < 2:
            print(" FUNCTION TAKES TWO ARGUMENTS!") 
            return
        else:
            try:    
                if not os.path.exists(arg[0]):
                    print(f"Error: The file {arg[0]} does not exist.")
                    return
                
                with zipfile.ZipFile(arg[1], "w", zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(arg[0], arcname=os.path.basename(arg[0]))
                    print(f"Successfully added {arg[0]} to {arg[1]}")
            except Exception as ERROR:
                print(f"ERROR:\n{ERROR}")

    def do_ping(self, arg):
        try:
            ping(arg, verbose=True)
        except Exception as ERROR:
            print(f"ERROR:\n{ERROR}")

    def do_wget(self, arg):
        """Gets a file from the web."""
        try:
            wget.download(arg)
            print()
        except Exception as ERROR:
            print(f"ERROR:\n{ERROR}")

    def do_arctar(self, arg):
        """Compresses tar."""
        arg = shlex.split(arg)
        if len(arg) < 2:
            print("THIS FUNCTION TAKES TWO ARGUMENTS!") 
            return
        else:
            try:
                if not os.path.exists(arg[0]):
                    print(f"Error: The file {arg[0]} does not exist.")
                    return
                
                with tarfile.open(arg[1], "w") as tarf:
                    tarf.add(arg[0], arcname=os.path.basename(arg[0]))
                    print(f"Successfully added {arg[0]} to {arg[1]}")
            except Exception as ERROR:
                print(f"ERROR:\n{ERROR}")

    def do_cut(self, arg):
        global Clipboard
        try:
            with open(arg, "r") as file: 
                Clipboard = file.read()
            print("Copied file {} sucsessfully.".format(Clipboard))
            os.remove(arg)
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_copy(self, arg):
        global Clipboard
        try:
            with open(arg, "r") as file: 
                Clipboard = file.read()
            print("Copied file {} sucsessfully.".format(Clipboard))

        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_paste(self, arg):
        global Clipboard
        try:
            if os.path.exists(arg): raise FileExistsError('FILE ALREADY EXISTS!')
            with open(arg, "w") as file:
                file.write(Clipboard)
                print("Pasted file {} sucsessfully.".format(arg))

        except FileExistsError as ERROR:
            print("FILE ALREADY EXISTS:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_distro(self, arg):
        """Prints out the current distro."""
        print(linux_distribution())

    def do_pendid(self, arg):
        """Ends a process by it's id."""
        try:
            parent = psutil.Process(int(arg))
            for child in parent.children(recursive=True):
                child.kill()
            parent.kill()
        except Exception as error:
            print(f"ERROR:\n{error}")

    def do_pend(self, arg):
        """End a process by it's name."""
        try:
            lib.general.endp(arg)
            print("Ended process sucsessfully")
        except Exception as error:
            print(f"ERROR:\n{error}")

    def do_ssh(self, arg):
        arg = shlex.split(arg)
        if len(arg) < 3:
            print("THIS FUNCTION TAKES THREE ARGUMENTS!") 
            return
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(arg[0], username=arg[1])
            stdin, stdout, stderr = ssh.exec_command(arg[2])
            print("Connected to {} successfully.".format(arg[0]))
            print("Command output:\n{}".format(stdout.read().decode()))
            print("Command error (if any):\n{}".format(stderr.read().decode()))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_animal(self, arg):
        match arg:
            case "dog":
                print(animallib.dog)
            case "cat":
                print(animallib.cat)
            case "cow":
                print(animallib.cow)
    
    def do_chperms(self, arg):
        """Changes the permissions of a file."""

        arg = shlex.split(arg)

        if len(arg) < 2:
            print("THIS FUNCTION TAKES TWO ARGUMENTS!") 
            return
        try:
            os.chmod(arg[0], int(arg[1], 8))
            print("Changed permissions of {} to {}.".format(arg[0], arg[1]))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))
    
    def do_chmod(self, arg):
        """Changes the permissions of a file."""
        self.do_chperms(arg)

    def do_tasks(self, arg):
        """Shows all of the tasks."""
        task_parser = argparse.ArgumentParser()
        task_parser.add_argument("-a", "--all", action="store_true", help="Show all tasks.")
        task_parser.add_argument("-s", "--simplified", action="store_true", help="Print a simplified version of tasks.")
        
        arg = arg.strip()
        
        try:
            args = task_parser.parse_args(arg.split())

            if args.all:
                print("Showing all tasks...")
                lib.general.list_processes_ws()
            elif args.simplified:
                print("Showing simplified tasks...")
                lib.general.list_processes_smp()
            elif not arg:
                print("No options selected. Showing default tasks...")
                lib.general.list_processes()
            else:
                print("Invalid arguments. Use -a for all tasks or -s for simplified tasks.")
        except SystemExit: return

    def do_dupe(self, arg):
        duper_parser = argparse.ArgumentParser(prog='dupe')
        duper_parser.add_argument(
            '-a', '--advanced', 
            action="store_true", 
            help="Duplicates in a more advanced way using copy2 (preserves metadata)."
        )
        duper_parser.add_argument('file', help="Path to the file to duplicate.")
        duper_parser.add_argument('new', help="New file's path.")

        arg = shlex.split(arg)
        
        if len(arg) < 2:
            print("THIS FUNCTION TAKES TWO ARGUMENTS!") 
            return

        try:
            args = duper_parser.parse_args(arg)
        except SystemExit:
            return

        try:
            if args.advanced:
                shutil.copy2(args.file, args.new)
                print(f"Advanced copy complete: {args.file} -> {args.new}")
            else:
                shutil.copy(args.file, args.new)
                print(f"Copy complete: {args.file} -> {args.new}")
        except FileNotFoundError as error:
            print(f"FILE NOT FOUND:\n{error}")
        except Exception as error:
            print(f"ERROR:\n{error}")


    def do_rename(self, arg):
        arg = shlex.split(arg)
        if len(arg) < 2:
            print("THIS FUNCTION TAKES TWO ARGUMENTS!") 
            return
        
        try:
            os.rename(arg[0], arg[1])
            print(f"Rename complete: {arg[0]} -> {arg[1]}")
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_mkdir(self, arg):
        """Creates a directory."""
        try:
            os.mkdir(arg)
            print("Created directory {} sucsessfully.".format(arg))
        except FileExistsError as ERROR:
            print("FILE ALREADY EXISTS:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))
    
    def do_mkf(self, arg):
        """Creates a file."""
        try:
            with open(arg, "x"): pass
            print("Created file {} sucsessfully.".format(arg))
        except FileExistsError as ERROR:
            print("FILE ALREADY EXISTS:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_cat(self, arg):
        try:
            with open(arg, "r") as file: 
                print(file.read())
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_getvar(self, arg): lib.general.getvar(arg)
    def do_setvar(self, arg): lib.general.setvar(arg)

    def do_read(self, arg): self.do_cat(arg)

    def do_append(self, arg):
        """
        Appends to a file.
        append "Hello, World!" test.txt
        """
        if len(arg) < 2: 
            print("THIS FUNCTION TAKES TWO ARGUMENTS!")
            return

        arg = shlex.split(arg)
        try:
            with open(arg[1], "a") as file: 
                file.write(arg[0])
                print("Appending completed.")
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_write(self, arg):
        """
        Writes to a file.
        write "Hello, World!" test.txt
        """
        if len(arg) < 2: 
            print("THIS FUNCTION TAKES TWO ARGUMENTS!")
            return

        arg = shlex.split(arg)
        mode = "w" if create_when_writing else "r+"
        try:
            with open(arg[1], mode) as file: 
                file.write(arg[0])
                print("Writing is completed.")
        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}\n Tip: You can create files with mkf command.".format(ERROR))
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_rm(self, arg):
        """Removes a file."""
        try:
            os.remove(arg)
            print(f"File {arg} removed successfully.")
        except FileNotFoundError:
            print(f"FILE NOT FOUND: {arg}\nTip: You can create files with the 'mkf' command.")
        except Exception as e:
            print(f"ERROR: {e}")

    def do_echo(self, arg): print(arg)

    def do_srch(self, arg):
        """Searches a file or a directory."""
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

    
    def do_debug(self, arg):
        try:
            exec(arg)
        except SystemExit: pass

    def do_usr(self, arg):
        """Prints out the current user."""
        print(getuser())

    def do_tree(self, arg):
        """Display the directory tree structure."""
        if not arg:
            print("Error: Please provide a directory path.")
            return

        if not os.path.isdir(arg):
            print(f"Error: '{arg}' is not a valid directory.")
            return

        for root, dirs, files in os.walk(arg):
            level = root.replace(arg, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}[{os.path.basename(root)}]")

            subindent = ' ' * 4 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")

    def do_ls(self, arg):
        """List the items in the current directory."""
        try:
            items = os.listdir(os.getcwd())
            
            ls_parser = argparse.ArgumentParser()
            ls_parser.add_argument("-c", "--count", action="store_true", help="Gives the count of items")
            ls_parser.add_argument("-l", "--long", action="store_true", help="Ls but with bunch of details.")
            ls_parser.add_argument("-lg","--legacy", action="store_true", help="Ls but old.")


            args = ls_parser.parse_args(arg.split())
            
            if args.count:
                print(len(items))
            elif args.long:
                print("\nPERMISSON  L O G     SIZE MODIFICATION ENTRY")
                lib.general.ls_long('.')
                print()
            elif args.legacy:
                for item in items:
                    print(item)
            else:
                for index, item in enumerate(items):
                    print("[{}] = {}".format(index, item))

        except SystemExit: return 
        
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_dir(self, arg):
        """Prints put the current directory."""
        print("CURRENT DIRECTORY: {}".format(os.getcwd()))
    
    def do_cwd(self, arg):
        """Prints put the current directory."""
        print("CURRENT DIRECTORY: {}".format(os.getcwd()))

    def do_pwd(self, arg):
        """Prints put the current directory."""
        print("CURRENT DIRECTORY: {}".format(os.getcwd()))

    def do_clr(self, arg):
        """Clears the screen."""
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(banner_type) if not clear_with_banner else None

    def do_clear(self, arg):
        """Clears the screen."""
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(banner_type) if not clear_with_banner else None

    def do_cls(self, arg):
        """Clears the screen."""
        os.system(CLEAR_PREFIX)
        BANNERS.print_banner_plus(banner_type) if not clear_with_banner else None

    def do_exit(self, arg):
        """Exits the command line interface."""
        os.system(CLEAR_PREFIX)
        return True

    def do_banner(self, arg):
        """Prints out the banner."""
        BANNERS.print_banner_plus(banner_type)
    
    def do_getopts(self, arg):
        """
        Gives options about a topic.
        Options:
            - banner (Prints all of the usable banners. If you want your own banner check out the guide in https://github.com/byTheInK/coterm/blob/main/md/makeabanner.md.)
            - ls
            - tasks
            - dupe
        """

        if arg.lower() == "banner":
            print(BANNERS.get_options(), "Don't put .txt in the settings.")
        elif arg.lower() == "ls":
            print("[-l, --long], [-lg, --legacy]")
        elif arg.lower() == "tasks":
            print("[-s, --simplified], [-a, --all]")
        elif arg.lower() == "dupe":
            print("[-a, --advanced]")
        else:
            print("NEEDS AN VALID OPTION TYPE. TYPE \"help getopts\".")
    
    def do_info(self, arg):
        """Gives information about the system."""
        try: 
            lib.advanced().top(arg)
        except SystemExit: pass
        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def do_sys(self, arg):
        """
        Uses your terminal to execute commands.
        sys notepad test.txt
        """
        try:
            os.system(arg)
        except Exception as ERROR:
            print("\n{}".format(ERROR))
                
    

    def do_random(self, arg):
        """Gives a random number between two numbers."""
        arg = arg.split()

        if len(arg) < 2:
            print("THIS FUNCTION TAKES TWO ARGUMENTS!")
            return
        try:
            print(random_number(int(arg[0]), int(arg[1])))
        except Exception as ERROR:
            print("ERROR:\n{} Please put integers if you didn't.".format(ERROR))


    def postcmd(self, stop, line):
        self.prompt = "{}>> ".format(os.getcwd())
        for i in range(space_after_command):
            print()
        return stop


    def do_settings(self, arg):
        global clear_with_banner
        global create_when_writing
        global line_per_page
        global banner_type
        global complete_key
        global space_after_command

        os.system(CLEAR_PREFIX)
        print("1: General")
        selection = input()

        if selection == "1":
            type, value = lib.config.general()

            if value == 1 and type == 1: 
                print("Please type a valid value")
                input("Press enter to continue")
                self.do_banner("")
                return

            if type == "CLEAR_WITH_BANNER": clear_with_banner = value
            if type == "CREATE_WHEN_WRITING": create_when_writing = value
            if type == "LINE_PER_PAGE": line_per_page = value
            if type == "BANNER_TYPE": banner_type = value
            if type == "SPACE_AFTER_COMMAND": space_after_command = value

            self.do_banner("")

if __name__ == "__main__":  
     coterm().cmdloop()
