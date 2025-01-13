#!/bin/bash
set -e
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

if ! command -v python3 &> /dev/null; then
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

if [ ! -f "$HOME/coterm" ]; then
    cp "$SCRIPT_DIR/coterm" "$HOME/coterm"
    chmod +x "$HOME/coterm"
    echo "Copied coterm script to $HOME."
else
    echo "coterm script already exists in $HOME."
fi

if ! grep -q 'export PATH="$HOME/coterm:$PATH"' ~/.bashrc; then
    echo 'export PATH="$HOME/coterm:$PATH"' >> ~/.bashrc
    echo "Updated PATH in ~/.bashrc."
else
    echo "PATH already updated in ~/.bashrc."
fi

echo "Setup complete."
deactivate