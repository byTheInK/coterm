# CoTerm

**CoTerm** is a versatile and customizable command-line interface (CLI) written in Python. It stands out with its unique features and extensive configuration options, making it an excellent choice for users who need a flexible and powerful tool for managing their terminal environments. It has a settings system which is not common in command-line-interfaces. It is not designed to be your main editor. It is mainly designed for scripting.

[!IMPORTANT]
CoTerm is designed to be used in Linux but you can find in the old versions.

## Key Features

- **Highly Customizable**: CoTerm offers a range of configuration options, enabling you to personalize the CLI to match your workflow and preferences.
- **Python Scripting Library**: CoTerm has a scripting library made for configruation and automation. With Python, you can create scripts really easily.
- **Beginer-Friendly**: Despite its powerful capabilities, CoTerm is designed to be intuitive and easy to use for both beginners and experienced users. If you don't understand a command, you can do "help \<commandname>". If you still don't understand a topic, you can read the markdown files.
- **Unusual Features**: CoTerm includes a variety of features not commonly found in traditional CLI tools, providing users with enhanced functionality.

# Installation

To get started with CoTerm, simply clone the repository and follow the installation instructions:

## First Part: Python
To install CoTerm you first need Python to be installed. Installation can change depending on your distribution.

### OpenSUSE
```bash
sudo zypper install python3
```

### Arch Linux
```bash
sudo pacman -S python3
```

### Ubuntu/Debian
```bash
sudo apt-get install python3
```

## Second Part: Git
You need Git because you have to clone the CoTerm Github repository. Again, this part depends on your Linux distribution.

### OpenSUSE
```bash
sudo zypper install git
```

### Arch Linux
```bash
sudo pacman -S git
```

### Ubuntu/Debian
```bash
sudo apt-get install git
```

## Final part: Cloning

```bash
cd ~
git clone https://github.com/byTheInK/coterm.git
cd coterm
source setup.sh
```

# Running
To run CoTerm, simply type the code below into your terminal.
```bash
bash coterm
```