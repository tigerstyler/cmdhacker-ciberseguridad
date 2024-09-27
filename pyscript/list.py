# list.py
import os

custom_commands_dir = r"C:\Users\tyler\programacion\Nuevacarpeta\cmdhacker\script"

def listar_comandos_personalizados():
    """Lista los comandos personalizados disponibles."""
    comandos = [archivo for archivo in os.listdir(custom_commands_dir) if archivo.endswith(".py") or archivo.endswith(".bat")]
    if comandos:
        print("\nComandos personalizados disponibles:")
        for comando in comandos:
            nombre, _ = os.path.splitext(comando)
            print(f" - {nombre}")
    else:
        print("Hmm... No tienes ningún comando personalizado aquí.\n")

if __name__ == "__main__":
    listar_comandos_personalizados()
