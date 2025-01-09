#!/bin/bash
SCRIPT_DIR=$(dirname "$(readlink -f "$0")") # Script'in bulunduğu dizini alır
"$SCRIPT_DIR/venv/bin/python" "$SCRIPT_DIR/main.py"