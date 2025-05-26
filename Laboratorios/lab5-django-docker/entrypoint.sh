#!/usr/bin/env bash

# Ejecutar migraciones antes de arrancar
python manage.py migrate --noinput

# Ejecutar collectstatic para archivos estáticos (opcional en dev)
python manage.py collectstatic --noinput

# Ejecutar el comando que se pase al contenedor (CMD)
exec "$@"
