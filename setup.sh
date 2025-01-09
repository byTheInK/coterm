#!/bin/bash

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

python3 -m venv "$SCRIPT_DIR/venv"
echo "Installed Python Virtual Environment."
sleep 2

source "$SCRIPT_DIR/venv/bin/activate"

"$SCRIPT_DIR/venv/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"
echo "Installed required packages."
sleep 2

export PATH="$~/coterm:$PATH"
echo "Successfully installed CoTerm"
sleep 1
