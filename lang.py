import argparse
from pathlib import Path
import importlib
import sys
import shlex

"""
parser = argparse.ArgumentParser(prog="Script handler")
parser.add_argument("file")
parsed = parser.parse_args()
"""

def main(file, args=""):
    module_name = Path(file).stem
    try:
        sys.path.append(str(Path(file).parent))
        
        module = importlib.import_module(module_name)
        
        if not hasattr(module, "main"):
            raise OSError(f"Error: The module '{module_name}' does not have a main function.")
        
        if hasattr(module, "args"):
            module.args = args

        module.main()
    except OSError as ERROR:
        print(ERROR)
    except Exception as e:
        print("ERROR: {}".format(e))
    finally:
        sys.path.remove(str(Path(file).parent))

if __name__ == "__main__":
    main("scripts\\myscript.py", [""])
