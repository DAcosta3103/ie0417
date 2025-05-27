# Documentación del Laboratorio 5 - IE0417

## Equipo
Diego Acosta  y Josué Zuniga 

---

## 1. Descripción General

Este laboratorio consiste en la creación y despliegue de una aplicación web básica usando Django, orquestada mediante Docker y Docker Compose con una base de datos PostgreSQL.  
El objetivo principal es lograr una solución dockerizada que incluya migraciones automáticas, gestión de variables de entorno y persistencia de datos.

---

## 2. Arquitectura del Proyecto

El proyecto está organizado con los siguientes componentes:

- *Servicio web (web):* Contenedor que ejecuta la aplicación Django, configurado para correr con Gunicorn y gestionado mediante un Dockerfile.  
- *Base de datos (db):* Contenedor PostgreSQL que almacena los datos persistentes.  
- *Red Docker:* Ambos contenedores están conectados a una red bridge llamada backend que permite comunicación segura.  
- *Volumen Docker:* Se usa un volumen dbdata para asegurar que los datos de la base de datos persistan aunque el contenedor se reinicie o elimine.

---

## 3. Descripción de Archivos Clave

### 3.1 Dockerfile

Define la imagen personalizada para la aplicación Django, basada en python:3.11-slim.  
Incluye la instalación de dependencias desde requirements.txt, la instalación de netcat-openbsd para la espera activa de la base de datos, copia del código fuente, y configuración del entrypoint.sh.

### 3.2 docker-compose.yml

Orquesta los servicios web y db, define las variables de entorno compartidas mediante un archivo .env, monta volúmenes para persistencia y define la red de comunicación entre contenedores.

### 3.3 entrypoint.sh

Script que se ejecuta al iniciar el contenedor web.  
Espera a que la base de datos esté lista usando nc, ejecuta migraciones, recoge archivos estáticos y luego arranca Gunicorn.

### 3.4 settings.py

Configuración de Django para conectarse a la base de datos PostgreSQL usando variables de entorno.  
Configura apps instaladas, middleware, rutas, y demás parámetros necesarios para la ejecución correcta.

### 3.5 core/views.py

Contiene la vista home que responde en la ruta raíz (/) con un mensaje simple para verificar que la app funciona correctamente.

---

## 4. Instrucciones de Ejecución

1. Colocarse en el directorio raíz del proyecto:

   ```bash
   cd lab5-docker-django
