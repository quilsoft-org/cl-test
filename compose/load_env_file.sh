#!/bin/bash
# -----------------------------------------------------------------------------
# Script: load_env_file_strict.sh
# Descripción:
#   Carga un archivo .env asegurándose de que todas las líneas sean válidas.
#   Las líneas válidas son del tipo VAR=valor (sin espacios alrededor del "=").
#   El script ignora comentarios (#), líneas vacías y entradas con "Host(".
#   Si encuentra líneas inválidas, muestra un error y termina con código 2.
# Uso:
#   source ./load_env_file_strict.sh path/a/.env
# -----------------------------------------------------------------------------


load_env_file_strict() {
  local env_file="$1"

  # Verificar que no se ejecute como root
  if [ "$EUID" -eq 0 ]; then
    echo "ERROR: Este script no debe ejecutarse como root."
    exit 1
  fi

  # Verificar que el usuario tenga UID y GID 1100
  local uid gid
  uid=$(id -u)
  gid=$(id -g)

  if [ "$uid" -ne 1100 ] || [ "$gid" -ne 1100 ]; then
    echo "ERROR: Este script debe ejecutarse con UID=1100 y GID=1100. UID actual: $uid, GID actual: $gid"
    exit 1
  fi

  if [ ! -f "$env_file" ]; then
    echo "ERROR: Archivo $env_file no encontrado."
    exit 1
  fi

  local missing_vars=()
  while IFS='=' read -r var _; do
    if [[ "$var" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      if ! grep -q "^$var=" "$env_file"; then
        missing_vars+=("$var")
      fi
    fi
  done < <(grep -v '^#' "$env_file")

  # Exportar todas las variables
  export $(grep -v '^#' "$env_file" | xargs -0)

  if [ ${#missing_vars[@]} -ne 0 ]; then
    echo "ERROR: Faltan variables en $env_file: ${missing_vars[*]}"
    exit 1
  fi
}

# Si se ejecuta directamente (no como source), correr con parámetro
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  load_env_file_strict "$1"
fi
