import os

def limpiar_pantalla():
    # Detectar el sistema operativo y ejecutar el comando apropiado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para otros sistemas operativos como Linux o MacOS
        os.system('clear')

def main():
    limpiar_pantalla()

if __name__ == "__main__":
    main()
