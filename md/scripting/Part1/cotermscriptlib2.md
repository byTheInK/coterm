"cotermscriptlib.py" is  python file designed to make scripting easier. This file is located in `$env:APPDATA\coterm\coterm\scripts\package\cotermscriptlib.py`. To reach this you can type `import package.cotermscriptlib as cotermscriptlib`. 


# Default
Default class contains the default values such as:,
```python
class default:
    clear_with_banner: bool = True
    create_when_writing: bool = True
    line_per_page: int = 15
    banner_type: str = "family"
    complete_key: str = "tab"
    space_after_command: int = 0
```

# Color
Color class has two parts. There is a **Foreground** class and a **Background class**. This allows you to write colored text.

***cotermscriptlib.py***
```python
class color:
    class Foreground:
        RED: str = colorama.Fore.RED
        GREEN: str = colorama.Fore.GREEN
        YELLOW: str = colorama.Fore.YELLOW
        BLUE: str = colorama.Fore.BLUE
        MAGENTA: str = colorama.Fore.MAGENTA
        CYAN: str = colorama.Fore.CYAN
        WHITE: str = colorama.Fore.WHITE
        BLACK: str = colorama.Fore.BLACK
        RESET: str = colorama.Fore.RESET
    
    class Background:
        RED: str = colorama.Back.RED
        GREEN: str = colorama.Back.GREEN
        YELLOW: str = colorama.Back.YELLOW
        BLUE: str = colorama.Back.BLUE
        MAGENTA: str = colorama.Back.MAGENTA
        CYAN: str = colorama.Back.CYAN
        WHITE: str = colorama.Back.WHITE
        BLACK: str = colorama.Back.BLACK
        RESET: str = colorama.Back.RESET
```

***myscript.py***
```python
import package.cotermscriptlib as ctlib

def main():
    print(ctlib.color.Foreground.RED+"Foreground")
    print(ctlib.color.Background.WHITE+"Background")
```

# Script
Script class has many things to help you such as: banner function, temporary file functions

# Errors
This part contains the coterm errors

```python
class Errors:
    Coterm404 = lib.CoTermErrors.CoTerm404
    CoTermPkgError = lib.CoTermErrors.CoTermPkgError
    CotermExtraError = lib.CoTermErrors.CotermExtraError
    CotermArgError = lib.CoTermErrors.CotermArgError
```