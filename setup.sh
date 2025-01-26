#!/bin/bash
set -e
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
cd $SCRIPT_DIR

if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed."
    exit 1
fi

python3 -m venv "./venv"
echo "Installed Python Virtual Environment."
sleep 2

source "./venv/bin/activate"

if ! "./venv/bin/pip" install --upgrade pip; then
    echo "Failed to upgrade pip."
    exit 1
fi

if ! "./venv/bin/pip" install -r "./requirements.txt"; then
    echo "Failed to install required packages."
    exit 1
fi

echo "Installed required packages."
sleep 2

chmod +x "$HOME/coterm/coterm"
echo "{}" > variabes.json

cp coterm /usr/bin/

echo "Setup complete."
deactivate
