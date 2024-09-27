import os
import subprocess
import platform
from datetime import datetime
import importlib

# Carga de módulos -> Load modules
cmd_stdlib = importlib.import_module('cmd', package=None)
# Directorio de Scripts -> Scripts directory
custom_commands_dir = "C:/Users/tyler/programacion/Nuevacarpeta/cmdhacker/pyscript" if os.name == 'nt' else "/home/tyler/programacion/Nuevacarpeta/cmdhacker/pyscript"  # Directorio de comandos personalizados
log_file = "logs/command_logs.txt"  # Archivo de registro de comandos
max_log_size = 5 * 1024  # Tamaño máximo del archivo de log en bytes (5 KB)

# Extensiones soportadas
supported_extensions = [".py", ".bat", ".sh", ".exe", ".cmd", ".pl", ".rb"]

def verificar_directorio_comandos():
    """Verifica si el directorio de comandos personalizados existe."""
    if not os.path.exists(custom_commands_dir):
        print(f"ERROR: El directorio '{custom_commands_dir}' no existe.")
        return False
    return True

def buscar_comando(comando):
    """Busca el comando en el directorio personalizado."""
    if not verificar_directorio_comandos():
        return None
    
    for archivo in os.listdir(custom_commands_dir):
        nombre, extension = os.path.splitext(archivo)
        if nombre.lower() == comando.lower() and extension in supported_extensions:
            return os.path.join(custom_commands_dir, archivo)
    return None

def rotar_logs():
    """Realiza la rotación de logs si el archivo actual excede el tamaño máximo."""
    if os.path.exists(log_file) and os.path.getsize(log_file) >= max_log_size:
        # Mover el archivo actual a un archivo con un timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nuevo_nombre = f"{log_file}_{timestamp}"
        os.rename(log_file, nuevo_nombre)
        print(f"El log ha sido rotado. Nuevo archivo: {nuevo_nombre}")

def registrar_log(comando, resultado):
    """Registra los comandos ejecutados y sus resultados en un archivo de log."""
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))  # Crea el directorio de logs si no existe
    
    rotar_logs()  # Ejecuta la rotación si es necesario
    with open(log_file, "a") as log:
        log.write(f"[{datetime.now()}] Comando: {comando} | Resultado: {resultado}\n")

def ejecutar_comando(comando):
    """Ejecuta un comando personalizado o del sistema."""
    comando_path = buscar_comando(comando)
    if comando_path:
        try:
            subprocess.run(comando_path, shell=True, check=True)
            registrar_log(comando, "Éxito")
        except subprocess.CalledProcessError as e:
            print(f"ERROR: El comando '{comando}' falló con el código de retorno {e.returncode}. Detalles: {e}")
            registrar_log(comando, f"Falló con código {e.returncode}")
        except PermissionError:
            print(f"ERROR: Permisos insuficientes para ejecutar '{comando}'.")
            registrar_log(comando, "Permisos insuficientes")
    else:
        try:
            subprocess.run(comando, shell=True, check=True)
            registrar_log(comando, "Éxito")
        except subprocess.CalledProcessError as e:
            print(f"'{comando}' no es reconocido. Error: {e}")
            registrar_log(comando, f"Falló con código {e.returncode}")
        except FileNotFoundError:
            print(f"Comando '{comando}' no encontrado.")
            registrar_log(comando, "Comando no encontrado")

def listar_comandos_personalizados():
    """Lista los comandos personalizados disponibles."""
    if not verificar_directorio_comandos():
        return
    
    comandos = [archivo for archivo in os.listdir(custom_commands_dir) if os.path.splitext(archivo)[1] in supported_extensions]
    if comandos:
        print("\nComandos personalizados disponibles:")
        for comando in comandos:
            nombre, _ = os.path.splitext(comando)
            print(f" - {nombre}")
    else:
        print("No tienes ningún comando personalizado aquí.")

def mostrar_ayuda():
    """Muestra los comandos del sistema disponibles."""
    print(f"""
    Comandos disponibles (Sistema: {platform.system()}):
    
    ASSOC         Manipula las asociaciones de archivos (Windows).
    CD            Cambia el directorio actual.
    CLS           Limpia la pantalla (Windows).
    COLOR         Cambia los colores de la consola (Windows).
    apt-get       Instala o desinstala paquetes (Linux/Mac).
    sudo          Ejecuta con privilegios elevados (Linux/Mac).
    git clone     Clona repositorios.
    list          Muestra los comandos personalizados disponibles.
    cwd           Muestra el directorio de comandos personalizados actual.
    help          Muestra este menú de ayuda.
    salir         Desconecta del sistema.
    """)

def mostrar_directorio_comandos():
    """Muestra el directorio actual de los comandos personalizados."""
    if verificar_directorio_comandos():
        print(f"Directorio de comandos personalizados: {custom_commands_dir}\n")

def main():
    print(f"(c) Darknet Corporation. Todos los derechos reservados.\n[Versión 1.0beta para {platform.system()}]\n")

    while True:
        current_directory = os.getcwd()
        comando = input(f"{current_directory}> ").strip()

        if comando.lower() in ["exit", "salir"]:
            print("Saliendo del sistema... Desconectado.")
            registrar_log(comando, "Sistema desconectado")
            break
        elif comando.lower() == "help":
            mostrar_ayuda()
        elif comando.lower() == "list":
            listar_comandos_personalizados()
        elif comando.lower() == "cwd":
            mostrar_directorio_comandos()
        elif comando:
            ejecutar_comando(comando)
        else:
            print("Debes introducir algo.")

if __name__ == "__main__":
    main()