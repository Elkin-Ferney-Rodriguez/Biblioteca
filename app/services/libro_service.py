from typing import List, Optional
from app.models.libro import Libro

class LibroService:
    """Clase para gestionar las operaciones relacionadas con libros en la biblioteca.

    Esta clase proporciona métodos para administrar el ciclo de vida de los libros,
    incluyendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y búsquedas.

    Attributes:
        libros (List[Libro]): Lista de todos los libros en el sistema
        usuarios (List[Usuario]): Lista de todos los usuarios registrados
    """

    def __init__(self):
        """Inicializa las listas de libros y usuarios del sistema."""
        self.libros: List[Libro] = []
        self.usuarios: List[Usuario] = []

    def agregar_libro(self, libro: Libro) -> bool:
        """Agrega un nuevo libro al sistema.

        Args:
            libro (Libro): Objeto libro a agregar al sistema

        Returns:
            bool: True si el libro fue agregado exitosamente, False si ya existe
        """
        if self.buscar_libro(libro.id_libro):
            print(f"Libro con ID {libro.id_libro} ya existe.")
            return False
        self.libros.append(libro)
        print(f"Libro con ID {libro.id_libro} agregado.")
        return True

    def eliminar_libro(self, id_libro: int) -> bool:
        """Elimina un libro del sistema.

        Args:
            id_libro (int): ID del libro a eliminar

        Returns:
            bool: True si el libro fue eliminado exitosamente, False si no se encontró
        """
        libro = self.buscar_libro(id_libro)
        if libro:
            self.libros.remove(libro)
            print(f"Libro con ID {id_libro} eliminado.")
            return True
        print(f"Libro con ID {id_libro} no encontrado.")
        return False

    def actualizar_libro(self, libro: Libro) -> bool:
        """Actualiza los datos de un libro existente.

        Args:
            libro (Libro): Objeto libro con los datos actualizados

        Returns:
            bool: True si el libro fue actualizado exitosamente, False si no se encontró
        """
        libro_existente = self.buscar_libro(libro.id_libro)
        if libro_existente:
            libro_existente.titulo = libro.titulo
            libro_existente.autor = libro.autor
            libro_existente.categoria = libro.categoria
            return True
        print(f"Libro con ID {libro.id_libro} no se pudo encontrar para actualizar.")
        return False

    def buscar_libros(self, atributo: str, valor: str) -> List[Libro]:
        """Busca libros por coincidencia parcial en cualquier atributo.

        Args:
            atributo (str): Nombre del atributo a buscar (titulo, autor, categoria)
            valor (str): Valor a buscar en el atributo especificado

        Returns:
            List[Libro]: Lista de libros que coinciden con el criterio de búsqueda
        """
        resultados = []
        for libro in self.libros:
            if hasattr(libro, atributo):
                valor_libro = getattr(libro, atributo)
                # Convertimos ambos valores a string en minúscula
                if valor.lower() in str(valor_libro).lower():
                    resultados.append(libro)

        if not resultados:
            print(f"No se encontraron libros con {atributo} que contenga '{valor}'.")
        return resultados

    def buscar_libro(self, id_libro: int) -> Optional[Libro]:
        """Busca un libro específico por su ID.

        Args:
            id_libro (int): ID del libro a buscar

        Returns:
            Optional[Libro]: El libro encontrado o None si no existe
        """
        for libro in self.libros:
            if libro.id_libro == id_libro:
                return libro
        return None