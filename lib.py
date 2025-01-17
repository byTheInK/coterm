import os
import time
import stat
import bannerlib
import argparse
import psutil
import socket
import json
from shlex import split

CLEAR_PREFIX: str = "clear"
CURRENT: str = os.path.dirname(os.path.abspath(__file__))
NoProcess = psutil.NoSuchProcess
AccessDenied = psutil.AccessDenied
ZombieProcess = psutil.ZombieProcess


class CoTermErrors:
    class CoTermExtraError(Exception):
        def __init__(self, message=""):
            self.message = message
            super().__init__(self.message)

    class CoTermPkgError(Exception):
        def __init__(self, message=""):
            self.message = message
            super().__init__(self.message)

    class CoTermArgError(Exception):
        def __init__(self, message=""):
            self.message = message
            super().__init__(self.message)

    class CoTerm404(Exception):
        def __init__(self, message=""):
            self.message = message
            super().__init__(self.message)


class general:
    def endp(PROCNAME):
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()

    def ip():
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        selection = input("Do you really want to continue?(y/n)")
        if selection == "y":
            print("\nNAME: " + hostname)
            print("IP: " + IPAddr)

    def list_processes_smp():
        processes = psutil.process_iter(['pid', 'name', 'username'])

        for process in processes:
            try:
                pid = process.info['pid']
                name = process.info['name']
                username = process.info['username']

                print(f"PID: {pid}, Name: {name}, User: {username}")

            except (NoProcess, AccessDenied, ZombieProcess):
                pass

    def list_processes():
        processes = psutil.process_iter(
            [
                'pid', 
                'name',
                'username',
                'status',
                'cpu_percent',
                'memory_info',
                'create_time',
                'num_threads'
            ]
        )

        for process in processes:
            try:
                pid = process.info['pid']
                name = process.info['name']
                username = process.info['username']
                status = process.info['status']
                
                if status not in ['stopped', 'zombie']:
                    cpu_percent = process.info['cpu_percent']
                    memory_info = process.info['memory_info']
                    create_time = process.info['create_time']
                    num_threads = process.info['num_threads']
                    
                    print(f"PID: {pid}")
                    print(f"Name: {name}")
                    print(f"Username: {username}")
                    print(f"Status: {status}")
                    print(f"CPU Usage (%): {cpu_percent}")
                    print(f"Memory Usage (bytes): {memory_info.rss}")
                    print(f"Creation Time: {create_time}")
                    print(f"Number of Threads: {num_threads}")
                    print("-" * 40)
                    
            except (NoProcess, AccessDenied, ZombieProcess):
                pass

    def list_processes_ws():
        processes = psutil.process_iter(
            [
                'pid',
                'name',
                'username',
                'status',
                'cpu_percent',
                'memory_info',
                'create_time',
                'num_threads'
            ]
        )

        for process in processes:
            try:
                pid = process.info['pid']
                name = process.info['name']
                username = process.info['username']
                status = process.info['status']
                cpu_percent = process.info['cpu_percent']
                memory_info = process.info['memory_info']
                create_time = process.info['create_time']
                num_threads = process.info['num_threads']
                
                print(f"PID: {pid}")
                print(f"Name: {name}")
                print(f"Username: {username}")
                print(f"Status: {status}")
                print(f"CPU Usage (%): {cpu_percent}")
                print(f"Memory Usage (bytes): {memory_info.rss}")
                print(f"Creation Time: {create_time}")
                print(f"Number of Threads: {num_threads}")
                print("-" * 40)
                
            except (NoProcess, AccessDenied, ZombieProcess):
                pass

    def memory():
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        total = memory.total / (1024 ** 2)
        used = memory.used / (1024 ** 2)
        free = memory.free / (1024 ** 2)
        available = memory.available / (1024 ** 2)
        percent = memory.percent

        swap_total = swap.total / (1024 ** 2)
        swap_used = swap.used / (1024 ** 2) 
        swap_free = swap.free / (1024 ** 2) 

        print(f"Total: {total:.2f} MB")
        print(f"Used: {used:.2f} MB")
        print(f"Free: {free:.2f} MB")
        print(f"Available: {available:.2f} MB")
        print(f"Memory Usage: {percent}%")

        print(f"\nSwap Total: {swap_total:.2f} MB")
        print(f"Swap Used: {swap_used:.2f} MB")
        print(f"Swap Free: {swap_free:.2f} MB")

    def pagerfirst(text, lines_per_page=15):
        lines = text.splitlines()
        total_lines = len(lines)
        current_line = 0

        while current_line < total_lines:
            os.system(CLEAR_PREFIX)
            for i in range(current_line, min(current_line + lines_per_page, total_lines)):
                print(lines[i])
            current_line += lines_per_page

            if current_line < total_lines:
                input("(Press Enter to continue or Ctrl+C to exit)")

        input("(Press Enter to continue or Ctrl+C to exit)")
        os.system(CLEAR_PREFIX)

    def getvar(arg):
        try:
            with open("variables.json", "r") as file:
                file = json.load(file)

                try:
                    print(file[arg])
                    return file[arg]

                except KeyError as ERROR:
                    print("KEY ERROR:\n{}".format(ERROR))

        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))

        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def setvar(arg):
        try:
            try:
                with open("variables.json", "r") as file:
                    data = json.load(file)

            except json.JSONDecodeError:
                data = {}

            key, value = split(arg)
            data[key] = value

            with open("variables.json", "w") as file:
                json.dump(data, file)

        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))

        except Exception as ERROR:
            print("ERROR:\n{}".format(ERROR))

    def ls_long(dir):
        try:
            entries = os.listdir(dir)

        except FileNotFoundError as ERROR:
            print("FILE NOT FOUND:\n{}".format(ERROR))
            return

        except PermissionError as ERROR:
            print("PERMISSION DENIED:\n{}".format(ERROR))
            return

        for entry in entries:
            full_path = os.path.join(dir, entry)

            try:
                stats = os.stat(full_path)

            except FileNotFoundError:
                continue

            except PermissionError:
                print("PERMISSION DENIED:\n{}".format(ERROR))
                continue

            mode = stats.st_mode
            file_type = '-' if stat.S_ISREG(mode) else 'd' if stat.S_ISDIR(mode) else 'l' if stat.S_ISLNK(mode) else '?'

            permissions = ''.join([
                'r' if mode & mask else '-'
                for mask in (stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR,
                            stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP,
                            stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH)
            ])

            permission_str = f"{file_type}{permissions}"

            hard_links = stats.st_nlink

            owner = f"{stats.st_uid}"

            group = f"{stats.st_gid}"
            size = stats.st_size

            mtime = time.strftime('%b %d %H:%M', time.localtime(stats.st_mtime))

            
            print(f"{permission_str} {hard_links} {owner} {group} {size:>8} {mtime} {entry}")

class advanced:
    def top(self, arg):
        parser = argparse.ArgumentParser(prog='top', description='Display system information.')
        parser.add_argument('-c', '--cpu', action='store_true', help='Show CPU usage.')
        parser.add_argument('-m', '--memory', action='store_true', help='Show memory usage.')
        parser.add_argument('-d', '--disk', action='store_true', help='Show disk usage.')
        parser.add_argument('-n', '--network', action='store_true', help='Show network usage.')
        
        args = parser.parse_args(arg.split())
        
        if args.cpu:
            print("CPU Usage:")
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                print(f"  CPU {i}: {percentage}%")
            print(f"  Total CPU: {psutil.cpu_percent(interval=1)}%")
        
        if args.memory:
            mem = psutil.virtual_memory()
            print("Memory Usage:")
            print(f"  Total: {mem.total / (1024 ** 3):.2f} GB")
            print(f"  Available: {mem.available / (1024 ** 3):.2f} GB")
            print(f"  Used: {mem.used / (1024 ** 3):.2f} GB")
            print(f"  Percentage: {mem.percent}%")
        
        if args.disk:
            print("Disk Usage:")
            for partition in psutil.disk_partitions():
                usage = psutil.disk_usage(partition.mountpoint)
                print(f"  {partition.device} ({partition.mountpoint}):")
                print(f"    Total: {usage.total / (1024 ** 3):.2f} GB")
                print(f"    Used: {usage.used / (1024 ** 3):.2f} GB")
                print(f"    Free: {usage.free / (1024 ** 3):.2f} GB")
                print(f"    Percentage: {usage.percent}%")
        
        if args.network:
            net_io = psutil.net_io_counters()
            print("Network Usage:")
            print(f"  Bytes Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
            print(f"  Bytes Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")
        
        if not (args.cpu or args.memory or args.disk or args.network):
            parser.print_help()

class config:
    def initialize_config():
        config_dict = {}

        with open(f"{CURRENT}/.settings/.CLEAR_WITH_BANNER", "r") as file:
            config_dict["CLEAR_WITH_BANNER"] = True if file.read() == "true" else False

        with open(f"{CURRENT}/.settings/.CREATE_WHEN_WRITING", "r") as file:
            config_dict["CREATE_WHEN_WRITING"] = True if file.read() == "true" else False

        with open(f"{CURRENT}/.settings/.LINE_PER_PAGE", "r") as file:
            config_dict["LINE_PER_PAGE"] = int(file.read())

        with open(f"{CURRENT}/.settings/.BANNER_TYPE", "r") as file:
            config_dict["BANNER_TYPE"] = file.read()

        with open(f"{CURRENT}/.settings/.SPACE_AFTER_COMMAND", "r") as file:
            config_dict["SPACE_AFTER_COMMAND"] = file.read()

        return config_dict

    def general():
        os.system(CLEAR_PREFIX)
        print("Settings")
        print("1: Clear with banner")
        print("2: Create when writing")
        print("3: Line per page")
        print("4: Banner type")
        print("5: Space after command")

        selection = input()

        if selection == "1":
            os.system(CLEAR_PREFIX)
            selection = input("Clear with banner: (true/false) ")
            
            if selection.lower() == "true":
                with open(f"{CURRENT}/.settings/.CLEAR_WITH_BANNER", "w") as file:
                    file.write(selection.lower())
                
                return "CLEAR_WITH_BANNER", True

            if selection.lower() == "false": 
                with open(f"{CURRENT}/.settings/.CLEAR_WITH_BANNER", "w") as file:
                    file.write(selection.lower())

                return "CLEAR_WITH_BANNER", False

            else: return 1, 1
        
        elif selection == "2":
            os.system(CLEAR_PREFIX)
            selection = input("Create when writing: (true / false) ")

            if selection.lower() == "true": 
                with open(f"{CURRENT}/.settings/.CREATE_WHEN_WRITING", "w") as file:
                    file.write(selection.lower())

                return "CREATE_WHEN_WRITING", True
            if selection.lower() == "false":
                with open(f"{CURRENT}/.settings/.CREATE_WHEN_WRITING", "w") as file:
                    file.write(selection.lower())

                return "CREATE_WHEN_WRITING", False
            else: return 1, 1

        elif selection == "3":
            os.system(CLEAR_PREFIX)
            selection = input("Line per page: (integer / whole number) ")

            try: selection = int(selection)
            except Exception: return 1, 1

            with open(f"{CURRENT}/.settings/.LINE_PER_PAGE", "w") as file:
                file.write(str(selection))

            return "LINE_PER_PAGE", selection
        
        elif selection == "4":
            os.system(CLEAR_PREFIX)
            selection = input("Banner type: ({}) ".format(bannerlib.BANNERS.get_options()))

            if selection in bannerlib.BANNERS.get_options(): 
                with open(f"{CURRENT}/.settings/.BANNER_TYPE", "w") as file:
                    file.write(selection)

                return "BANNER_TYPE", selection
            
            else: return 1, 1

        elif selection == "5":
            os.system(CLEAR_PREFIX)
            selection = input("Space after command: (integer / whole number) ")

            try: selection = int(selection)
            except Exception: return 1, 1

            with open(f"{CURRENT}/.settings/.SPACE_AFTER_COMMAND", "w") as file:
                file.write(str(selection))

            return "SPACE_AFTER_COMMAND", selection
