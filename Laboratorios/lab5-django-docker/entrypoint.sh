#!/usr/bin/env bash
set -e

host="$DB_HOST"
port=5432

echo "Esperando a que la base de datos en $host:$port esté lista..."

until nc -z "$host" "$port"; do
  >&2 echo "Base de datos no disponible - esperando..."
  sleep 1
done

echo "Base de datos disponible - continuando."

# Ejecutar migraciones antes de arrancar
python manage.py migrate --noinput

# Ejecutar collectstatic para archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar el comando que se pase al contenedor (CMD)
exec "$@"
