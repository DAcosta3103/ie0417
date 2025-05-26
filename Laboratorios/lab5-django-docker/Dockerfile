FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Copia solo requirements primero para caché eficiente
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Instalar netcat-openbsd para wait-for-db en entrypoint.sh
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Copia todo el código
COPY . /code/

# ENTRYPOINT para migraciones automáticas
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
