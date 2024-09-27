import os
import subprocess
import sys

def main():
    if len(sys.argv) == 1:
        # Muestra el directorio actual usando el comando `cd` nativo
        subprocess.run("cd", shell=True)
    elif len(sys.argv) == 2:
        # Cambia el directorio usando el comando `cd` nativo
        directorio = sys.argv[1]
        subprocess.run(f"cd /d {directorio}", shell=True)
    else:
        print("Uso: CD [directorio]")

if __name__ == "__main__":
    main()
