#!/bin/bash

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

if ! command -v python3 &> /dev/null;  then
    echo "Python 3 is not installed."
    exit 1
fi

python3 -m venv "$SCRIPT_DIR/venv"
echo "Installed Python Virtual Environment."
sleep 2

source "$SCRIPT_DIR/venv/bin/activate"

if ! "$SCRIPT_DIR/venv/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"; then
    echo "Failed to install required packages."
    exit 1
fi

echo "Installed required packages."
sleep 2

if ! grep -q 'export PATH="~/coterm:$PATH"' ~/.bashrc; then
    echo 'export PATH="~/coterm:$PATH"' >> ~/.bashrc
    echo "Updated PATH in ~/.bashrc."
else
    echo "PATH already updated in ~/.bashrc."
fi

chmod +x "SCRIPT_DIR/coterm"

echo "Setup complete."