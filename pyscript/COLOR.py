import os
import sys

def cambiar_color(codigo_color):
    # Verifica si el código de color es válido
    if len(codigo_color) != 2 or not all(c in '0123456789ABCDEF' for c in codigo_color.upper()):
        print("Código de color no válido. Uso: COLOR [00-0F | 10-1F | ... | F0-FF]")
        return
    
    if os.name == 'nt':  # Solo funciona en Windows
        os.system(f'color {codigo_color}')
    else:
        print("El comando COLOR solo es compatible con Windows.")

def mostrar_ayuda():
    print("""
    Establece los colores de primer plano y de fondo predeterminados de la consola.
    
    COLOR [atributos]
    
    Atributos de color:
        0 = Negro       8 = Gris
        1 = Azul        9 = Azul claro
        2 = Verde       A = Verde claro
        3 = Aguamarina  B = Aguamarina claro
        4 = Rojo        C = Rojo claro
        5 = Púrpura     D = Púrpura claro
        6 = Amarillo    E = Amarillo claro
        7 = Blanco      F = Blanco brillante
    
    Ejemplo: COLOR 1E
    """)

def main():
    if len(sys.argv) == 2:
        cambiar_color(sys.argv[1])
    else:
        mostrar_ayuda()

if __name__ == "__main__":
    main()
