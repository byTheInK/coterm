# Creating a script
CoTerm uses `Python` as a scripting language. You can make lots of thing with CoTerm scripts such as AI assistant, automating commands, making and switching envoirments. Let's get started. To create a script, launch CoTerm and type `mkscript myfirstscript`. This will create a file called `myfirstscript.py`.

# Opening a script
- Open CoTerm and type `openscript myfirstscript`. This will open notepad
- Open CotTerm and type `sys code %APPDATA\coterm\coterm\scripts\myfirstscript.py`. You can change the `code` area if you want to use another command to open a script like `vim`.

# Meeting the scripting library
If you opened your editor paste these lines of code:
```python
import time
import package.cotermscriptlib as cotermscriptlib
args = []
pkg = {}

def main():
    print("args: ", args)
    print("pkg:", pkg)
    print("windows: ", cotermscriptlib.var.WINDOWS)
    print("Write an integer to set how many seconds you want to wait")
    duration = input(pkg.get("prompt"))
    time.sleep(int(duration))
    cotermscriptlib.script.banner(pkg.get("banner_type"))
```
## package.cotermscriptlib
`package.cotermscriptlib` is a Python file made for controlling general scripting.

## args
When we try to run this script we give arguments such as true, false, 10 etc. Args section contains these values.

## pkg
This area contains system information. In this script we get the prompt which is `mydirectory>>` in general and we get the banner type which is family in general.

## main
This area is where the code gets executed.