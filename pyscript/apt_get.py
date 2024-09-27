#!/usr/bin/env python3

import os
import sys
import platform
import time

def detectar_sistema_operativo():
    sistema = platform.system()
    if sistema == "Linux":
        distro = platform.linux_distribution()[0].lower()
        if "ubuntu" in distro or "debian" in distro:
            return "Debian"
        elif "fedora" in distro:
            return "Fedora"
        elif "centos" in distro or "rhel" in distro:
            return "CentOS"
        else:
            return "Linux"
    elif sistema == "Darwin":
        return "macOS"
    elif sistema == "Windows":
        return "Windows"
    else:
        return None

def comando_existente(comando):
    """Verifica si el comando existe en el sistema."""
    return os.system(f"command -v {comando}") == 0

def actualizar_indices(sistema):
    if sistema in ["Debian", "Linux"]:
        if comando_existente("apt-get"):
            print("Actualizando índices de paquetes en Linux (Debian)...")
            os.system("sudo apt-get update")
        elif comando_existente("dnf"):
            print("Actualizando índices de paquetes en Fedora...")
            os.system("sudo dnf update")
    elif sistema == "Fedora":
        print("Actualizando índices de paquetes en Fedora...")
        os.system("sudo dnf update")
    elif sistema == "CentOS":
        print("Actualizando índices de paquetes en CentOS...")
        os.system("sudo yum update")
    elif sistema == "macOS":
        print("Actualizando índices de paquetes en macOS...")
        os.system("brew update")
    elif sistema == "Windows":
        print("Actualizando índices de paquetes en Windows...")
        os.system("choco upgrade all -y")

def instalar_paquete(sistema, paquete):
    if sistema in ["Debian", "Linux"]:
        print(f"Instalando {paquete} en Linux (Debian)...")
        os.system(f"sudo apt-get install -y {paquete}")
    elif sistema == "Fedora":
        print(f"Instalando {paquete} en Fedora...")
        os.system(f"sudo dnf install -y {paquete}")
    elif sistema == "CentOS":
        print(f"Instalando {paquete} en CentOS...")
        os.system(f"sudo yum install -y {paquete}")
    elif sistema == "macOS":
        print(f"Instalando {paquete} en macOS...")
        os.system(f"brew install {paquete}")
    elif sistema == "Windows":
        print(f"Instalando {paquete} en Windows...")
        os.system(f"choco install {paquete} -y")

def eliminar_paquete(sistema, paquete, purge=False):
    if sistema in ["Debian", "Linux"]:
        if purge:
            print(f"Eliminando {paquete} junto con archivos de configuración en Linux (Debian)...")
            os.system(f"sudo apt-get purge -y {paquete}")
        else:
            print(f"Eliminando {paquete} en Linux (Debian)...")
            os.system(f"sudo apt-get remove -y {paquete}")
    elif sistema == "Fedora":
        print(f"Eliminando {paquete} en Fedora...")
        os.system(f"sudo dnf remove -y {paquete}")
    elif sistema == "CentOS":
        print(f"Eliminando {paquete} en CentOS...")
        os.system(f"sudo yum remove -y {paquete}")
    elif sistema == "macOS":
        print(f"Eliminando {paquete} en macOS...")
        os.system(f"brew uninstall {paquete}")
    elif sistema == "Windows":
        print(f"Eliminando {paquete} en Windows...")
        os.system(f"choco uninstall {paquete} -y")

def mostrar_ayuda():
    """Muestra los comandos disponibles y su uso."""
    print("""
Uso: apt_get <comando> [paquete]
Comandos disponibles:
    update           Actualiza los índices de paquetes.
    install [pkg]    Instala un paquete específico.
    remove [pkg]     Elimina un paquete sin borrar archivos de configuración.
    purge [pkg]      Elimina un paquete y borra todos sus archivos de configuración. (Solo Linux)
    """)

def main():
    sistema = detectar_sistema_operativo()
    if sistema is None:
        print("Sistema operativo no soportado.")
        return

    if len(sys.argv) < 2 or sys.argv[1] == "help":
        mostrar_ayuda()
        return

    comando = sys.argv[1]

    start_time = time.time()

    if comando == "update":
        actualizar_indices(sistema)
    elif comando == "install" and len(sys.argv) > 2:
        paquete = sys.argv[2]
        instalar_paquete(sistema, paquete)
    elif comando == "remove" and len(sys.argv) > 2:
        paquete = sys.argv[2]
        eliminar_paquete(sistema, paquete)
    elif comando == "purge" and len(sys.argv) > 2 and sistema in ["Debian", "Linux"]:
        paquete = sys.argv[2]
        eliminar_paquete(sistema, paquete, purge=True)
    else:
        print("Comando o uso incorrecto. Usa 'apt_get help' para más información.")

    end_time = time.time()
    print(f"Operación completada en {end_time - start_time:.2f} segundos.")

if __name__ == "__main__":
    main()
