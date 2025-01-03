from pathlib import Path
import importlib
import sys

def main(file, args: list, _conf_list: dict):
    module_name = Path(file).stem
    try:
        sys.path.append("scripts")
        module = importlib.import_module("scripts."+module_name)
        
        if not hasattr(module, "main"): raise OSError(f"Error: The module '{module_name}' does not have a main function.")
        if hasattr(module, "args"): module.args = args
        
        if hasattr(module, "pkg"):
            module.pkg = _conf_list

        module.main()
    except OSError as ERROR:
        print(ERROR)
    except Exception as e:
        print("ERROR: {}".format(e))