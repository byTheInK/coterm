from pathlib import Path
import importlib
from lib import CoTermErrors
import sys


def main(file, args: list, _conf_list: dict):
    module_name = Path(file).stem
    try:
        sys.path.append("scripts")
        module = importlib.import_module("scripts."+module_name)

        if not hasattr(module, "main"):
            raise CoTermErrors.CoTerm404

        if hasattr(module, "args"):
            if args is not list:
                raise CoTermErrors.CoTermArgError

            module.args = args

        if hasattr(module, "pkg"):
            module.pkg = _conf_list

            if args is not dict:
                raise CoTermErrors.CoTermPkgError

        module.main()

    except CoTermErrors.CoTerm404:
        print('Main function not found in "{}" script.'.format(module_name))
    except CoTermErrors.CoTermPkgError:
        print('Pkg is in an unknown type.')
    except CoTermErrors.CoTermArgError:
        print('Arg is in an unknown type.')
    except Exception as e:
        print("ERROR: {}".format(e))
