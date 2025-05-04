# Usa una imagen base de Python
FROM python:3.10-slim

# Actualiza la lista de paquetes e instala git
RUN apt-get update && apt-get install -y git

# Define el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Establece el PYTHONPATH para que Python pueda encontrar los módulos
ENV PYTHONPATH=/app:$PYTHONPATH

# Instala las dependencias desde el archivo requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Cambia los permisos de los archivos si es necesario
RUN chmod -R 755 /app

# Establece el comando por defecto para ejecutar el script main.py
CMD ["python", "/app/app/main.py"]
