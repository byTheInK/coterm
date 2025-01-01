from pathlib import Path
import importlib
import sys

def main(file, args, _conf_list):
    module_name = Path(file).stem
    try:
        sys.path.append("scripts")
        module = importlib.import_module("scripts."+module_name)
        
        if not hasattr(module, "main"): raise OSError(f"Error: The module '{module_name}' does not have a main function.")
        if hasattr(module, "args"): module.args = args
        
        if hasattr(module, "pkg"):
            module.pkg["prompt"] = _conf_list._prompt
            module.pkg["clear_with_banner"] = _conf_list._clear_with_banner
            module.pkg["create_when_writing"] = _conf_list._create_when_writing
            module.pkg["line_per_page"] = _conf_list._line_per_page
            module.pkg["banner_type"] = _conf_list._banner_type
            module.pkg["complete_key"] = _conf_list._complete_key

        module.main()
    except OSError as ERROR:
        print(ERROR)
    except Exception as e:
        print("ERROR: {}".format(e))