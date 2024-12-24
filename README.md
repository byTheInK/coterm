# CoTerm

**CoTerm** is a versatile and customizable command-line interface (CLI) written in Python. It stands out with its unique features and extensive configuration options, making it an excellent choice for users who need a flexible and powerful tool for managing their terminal environments. It has a settings system which is not common in command-line-interfaces.

## Warnings
- CoTerm only supports Windows operating system
- You need to install Git and Python before starting installation
- While making script files you shouldn't use library file names. (Example: test, numpy, time, random)
## Key Features

- **Highly Customizable**: CoTerm offers a range of configuration options, enabling you to personalize the CLI to match your workflow and preferences.
- **Python Scripting Library**: CoTerm has a scripting library made for configruation and automation. With Python, you can create scripts really easily.
- **Beginer-Friendly**: Despite its powerful capabilities, CoTerm is designed to be intuitive and easy to use for both beginners and experienced users. If you don't understand a command, you can do "help \<commandname>". If you still don't understand a topic, you can read the markdown files.
- **Unusual Features**: CoTerm includes a variety of features not commonly found in traditional CLI tools, providing users with enhanced functionality.

# Installation

To get started with CoTerm, simply clone the repository and follow the installation instructions:

## Open Windows PowerShell
- Press `Windows Key + R`
- Type `powershell` and press the enter key

## Python and Git installation
To install Coterm you need Git and Python to be installed. Here is a quick guide how to use them.

### Install Python
- Go to the [Python's website](https://www.python.org/)
- Go to the downloads tab and select Windows
- Install the latest Python release
- Go through the installation process
- WARNING: When installing Python check the `add to the Path` option

### Install Git
- Go to the [Git's website](https://git-scm.com/)
- Go to the downloads tab and select Windows
- Click 64 bit if you are in a modern computer else pick the 32 bit one (You may need to look at It)
- Go through the installation process

## Cloning the Github Repository
```bash
mkdir $env:APPDATA\coterm
cd $env:APPDATA\coterm
git clone https://github.com/byTheInK/coterm.git
cd .\coterm
pip install -r requirements.txt
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:APPDATA\coterm\coterm", [EnvironmentVariableTarget]::Machine)
```
After this close and open the terminal and type `coterm`.
