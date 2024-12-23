import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).parent.parent.parent))

import bannerlib
import lib

class var:
    WINDOWS: bool = os.name == "nt"
    CLEAR_PREFIX: str = "cls"
    COTERM_DIR: str = lib.CURRENT

class script:
    def banner(TYPE): bannerlib.BANNERS.print_banner_plus(TYPE)
    