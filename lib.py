import psutil.psutil as psutil
import os
import time
import stat

WINDOWS: bool = os.name == "nt"
CLEAR_PREFIX: str = "cls" if WINDOWS else "clear"

class general:
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

    def deattach_process(path):
        deattached = []
        path = os.path.abspath(path)

        for process in psutil.process_iter(['pid', 'name', 'open_files']):
            try:
                open_files = process.info['open_files']

                if open_files:
                    for f in open_files:
                        if f.path == path:

                            print(f"Terminating process {process.info['name']} (PID: {process.info['pid']}) using {path}")
                            process.terminate()
                            deattached.append(process.info['pid'])
                            
            except psutil.AccessDenied:
                print("There are procsesses can't be deattached. Please run your terminal as an administrator if you accept the risks.")

            except psutil.NoSuchProcess: continue

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

            except FileNotFoundError: continue

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

            owner = f"{stats.st_uid}"  # Change this to use pwd.getpwuid(stats.st_uid).pw_name

            group = f"{stats.st_gid}"
            size = stats.st_size

            mtime = time.strftime('%b %d %H:%M', time.localtime(stats.st_mtime))

            
            print(f"{permission_str} {hard_links} {owner} {group} {size:>8} {mtime} {entry}")