# Sistema de Gestión de Biblioteca

Este proyecto es un **Sistema de Gestión de Biblioteca** desarrollado en Python. Permite gestionar libros, usuarios y préstamos de manera eficiente. El sistema incluye funcionalidades como agregar, eliminar, actualizar y buscar libros y usuarios, así como realizar préstamos y devoluciones.

## Características

- **Gestión de Libros**: Agregar, eliminar, actualizar y buscar libros.
- **Gestión de Usuarios**: Registrar, eliminar, actualizar y buscar usuarios.
- **Préstamos y Devoluciones**: Realizar préstamos de libros a usuarios y registrar devoluciones.
- **Historial y Estado**: Mantener un historial de préstamos y verificar la disponibilidad de libros.
- **Ordenamiento**: Listar libros ordenados por diferentes criterios (ID, título, autor, categoría, disponibilidad).

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.9+**
- **Git** (para clonar el repositorio)
- **Docker** y **Docker Compose** (opcional, para ejecutar el proyecto en un contenedor)

---

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Elkin-Ferney-Rodriguez/Biblioteca.git
cd Biblioteca
2. Configuración del Entorno Virtual (opcional)
Es recomendable usar un entorno virtual para instalar las dependencias:

bash
Copy Code
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instalar Dependencias
Instala las dependencias necesarias desde el archivo requirements.txt:

bash
Copy Code
pip install -r requirements.txt
4. Ejecutar el Proyecto
Ejecuta el programa principal:

bash
Copy Code
python app/main.py
Uso del Sistema
Al ejecutar el programa, se mostrará un menú interactivo con las siguientes opciones:

Menú Principal
Gestión de Libros: Permite agregar, eliminar, actualizar, buscar y listar libros.
Gestión de Usuarios: Permite registrar, eliminar, actualizar y buscar usuarios.
Préstamos y Devoluciones: Permite realizar préstamos y registrar devoluciones de libros.
Salir: Finaliza el programa.
Ejemplo de Flujo
Agrega un libro ingresando su ID, título, autor y categoría.
Registra un usuario ingresando su ID, nombre y correo electrónico.
Realiza un préstamo seleccionando un libro y un usuario.
Devuelve el libro cuando el usuario lo regrese.
Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

/app
├── app/
│   ├── __init__.py
│   ├── main.py                # Archivo principal del programa
│   ├── models/                # Clases que representan entidades del sistema
│   │   ├── __init__.py
│   │   ├── libro.py           # Clase Libro
│   │   └── usuario.py         # Clase Usuario
│   ├── services/              # Lógica de negocio y operaciones
│   │   ├── __init__.py
│   │   ├── libro_service.py   # Gestión de libros
│   │   ├── usuarioservice.py  # Gestión de usuarios
│   │   └── prestamos_services.py # Gestión de préstamos y devoluciones
├── tests/                     # Pruebas unitarias
│   ├── __init__.py
│   ├── test_models.py         # Pruebas para las clases de modelos
│   └── test_services.py       # Pruebas para los servicios
├── data/                      # Carpeta para almacenar datos (opcional)
├── Dockerfile                 # Configuración de Docker
├── docker-compose.yml         # Configuración de Docker Compose
├── setup.py                   # Configuración del paquete Python
└── biblioteca.egg-info/       # Información del paquete instalado
Ejecución con Docker
Si prefieres usar Docker, sigue estos pasos:

1. Construir la Imagen
Construye la imagen de Docker:

bash
Copy Code
docker build -t biblioteca .
2. Ejecutar el Contenedor
Ejecuta el contenedor:

bash
Copy Code
docker run -it --rm biblioteca
3. Usar Docker Compose
También puedes usar docker-compose para simplificar la ejecución:

bash
Copy Code
docker-compose up
Pruebas
El proyecto incluye pruebas unitarias para garantizar la calidad del código. Para ejecutarlas, usa:

bash
Copy Code
python -m unittest discover -s tests
Contribuciones
¡Las contribuciones son bienvenidas! Si deseas colaborar, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz un commit (git commit -m 'Agrega nueva funcionalidad').
Haz un push a tu rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Autor
Desarrollado por Elkin Ferney Rodriguez.

Contacto
Si tienes preguntas o sugerencias, no dudes en contactarme:

Correo: rodriguez.elkinferney@outlook.com
GitHub: Elkin-Ferney-Rodriguez
