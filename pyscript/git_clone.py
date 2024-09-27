#!/usr/bin/env python3

import os
import sys
import subprocess

def git_clone(repo_url, target_dir=None):
    comando = ["git", "clone", repo_url]
    if target_dir:
        comando.append(target_dir)
    
    try:
        subprocess.run(comando, check=True)
        print(f"Repositorio clonado exitosamente desde {repo_url}")
    except subprocess.CalledProcessError:
        print(f"Error al clonar el repositorio desde {repo_url}")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Uso: git_clone <repo_url> [directorio_destino]")
        return
    
    repo_url = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) == 3 else None
    
    git_clone(repo_url, target_dir)

if __name__ == "__main__":
    main()
