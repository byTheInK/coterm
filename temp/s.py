import cmd
import argparse

class MyCLI(cmd.Cmd):
    intro = 'Welcome to MyCLI. Type help or ? to list commands.\n'
    prompt = '(mycli) '
    
    def do_compile(self, arg):
        """Compile a file with options."""
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file', required=True, help='Input file to compile')
        parser.add_argument('-o', '--output', required=True, help='Output file')
        parser.add_argument('--nostdlib', action='store_true', help='Do not include standard library')
        
        # Parse the arguments
        args = parser.parse_args(arg.split())
        
        # Implement the compile functionality here
        
        print(f"Compiling file {args.file} to {args.output}...")
        if args.nostdlib:
            print("Standard library will not be included.")
        # Add your actual compile logic here

    def do_exit(self, arg):
        """Exit the CLI."""
        print("Exiting MyCLI.")
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()
