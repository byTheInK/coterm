#!/bin/bash
set -e
cd ~/coterm

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

if ! grep -q 'export PATH="$HOME/coterm:$PATH"' ~/.bashrc; then
    echo 'export PATH="$HOME/coterm:$PATH"' >> ~/.bashrc
    echo "Updated PATH in ~/.bashrc."
else
    echo "PATH already updated in ~/.bashrc."
fi

chmod +x "$HOME/coterm/coterm"

echo "Setup complete."
deactivate