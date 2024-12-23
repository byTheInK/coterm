import time
import package.cotermscriptlib as cotermscriptlib
args = []
pkg = {}

def main():
    print("pkg:", pkg)
    print("windows: ", cotermscriptlib.var.WINDOWS)
    print("Write an integer to set how many seconds you want to wait")
    duration = input(pkg.get("prompt"))
    time.sleep(int(duration))
    cotermscriptlib.script.banner(pkg.get("banner_type"))

if __name__ == "__main__":
    ...
    # Add here the main function and set the pkg args