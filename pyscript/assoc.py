import os
import sys
import winreg

def listar_asociaciones():
    print("Asociaciones de extensiones de archivos:\n")
    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "") as key:
        i = 0
        while True:
            try:
                subkey_name = winreg.EnumKey(key, i)
                if subkey_name.startswith("."):
                    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, subkey_name) as subkey:
                        value, _ = winreg.QueryValueEx(subkey, "")
                        print(f"{subkey_name} -> {value}")
                i += 1
            except OSError:
                break

def modificar_asociacion(extension, programa):
    try:
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, extension) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, programa)
        print(f"Asociación de {extension} cambiada a {programa}.")
    except Exception as e:
        print(f"Error al modificar la asociación: {e}")

def main():
    if len(sys.argv) == 1:
        listar_asociaciones()
    elif len(sys.argv) == 3:
        extension = sys.argv[1]
        programa = sys.argv[2]
        modificar_asociacion(extension, programa)
    else:
        print("Uso: ASSOC [extensión] [programa]")
        print("Ejemplos:")
        print("  ASSOC .txt txtfile")
        print("  ASSOC .py Python.File")

if __name__ == "__main__":
    main()
