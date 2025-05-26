# Informe Técnico - Laboratorio 5 IE0417

## Objetivo
Desplegar una aplicación Django usando Docker y Docker Compose, con base de datos PostgreSQL, red personalizada y persistencia.

## Arquitectura del Sistema
- 1 contenedor Django (web)
- 1 contenedor PostgreSQL (db)
- Red Docker personalizada `backend`
- Volumen `postgres_data` para persistencia de datos

## Archivos Clave

### Dockerfile
Contiene las instrucciones para crear la imagen personalizada de Django.

### docker-compose.yml
Orquesta los servicios `web` y `db`, define red, volumen y variables de entorno.

### .env
Define variables como nombre de base de datos, usuario y contraseña (no reales).

### requirements.txt
Lista las dependencias de Python: Django, Gunicorn y PostgreSQL.

## Instrucciones para ejecución

```bash
docker-compose up --build
```

Esto crea los contenedores y expone la app en http://localhost:8000

## Capturas
> (Aquí se deben incluir capturas reales de la app corriendo)
