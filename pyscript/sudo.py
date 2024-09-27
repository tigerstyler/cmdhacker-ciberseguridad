import os
import sys
import platform
import subprocess

def ejecutar_como_administrador(comando):
    sistema = platform.system()

    if sistema == "Linux" or sistema == "Darwin":  # Linux o macOS
        # Usar sudo en Linux o macOS
        comando_con_sudo = f"sudo {' '.join(comando)}"
        os.system(comando_con_sudo)

    elif sistema == "Windows":
        # Usar runas en Windows
        comando_con_runas = f"runas /noprofile /user:Administrator \"{' '.join(comando)}\""
        os.system(comando_con_runas)

    else:
        print("Sistema operativo no soportado.")

def main():
    if len(sys.argv) < 2:
        print("Uso: sudo <comando>")
        return

    comando = sys.argv[1:]
    ejecutar_como_administrador(comando)

if __name__ == "__main__":
    main()
