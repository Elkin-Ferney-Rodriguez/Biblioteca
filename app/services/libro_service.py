from typing import List, Optional
from app.models.libro import Libro
from app.structures.binary_search_tree import BinarySearchTree

class LibroService:
    """Clase para gestionar las operaciones relacionadas con libros en la biblioteca.

    Esta clase proporciona métodos para administrar el ciclo de vida de los libros,
    incluyendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y búsquedas.

    Attributes:
        libros_por_id (BinarySearchTree): Árbol binario de búsqueda para libros por ID
        libros_por_titulo (BinarySearchTree): Árbol binario de búsqueda para libros por título
    """

    def __init__(self):
        """Inicializa los árboles binarios de búsqueda para libros."""
        self.libros_por_id = BinarySearchTree()
        self.libros_por_titulo = BinarySearchTree()

    def agregar_libro(self, libro: Libro) -> bool:
        """Agrega un nuevo libro al sistema.

        Args:
            libro (Libro): Objeto libro a agregar al sistema

        Returns:
            bool: True si el libro fue agregado exitosamente, False si ya existe
        """
        # Intentar insertar en el árbol por ID
        if self.libros_por_id.insert(libro, lambda x: x.id_libro):
            # Si se insertó correctamente, agregarlo también al árbol por título
            self.libros_por_titulo.insert(libro, lambda x: x.titulo.lower())
            print(f"Libro con ID {libro.id_libro} agregado.")
            return True
        print(f"Libro con ID {libro.id_libro} ya existe.")
        return False

    def eliminar_libro(self, id_libro: int) -> bool:
        """Elimina un libro del sistema.

        Args:
            id_libro (int): ID del libro a eliminar

        Returns:
            bool: True si el libro fue eliminado exitosamente, False si no se encontró
        """
        # Por ahora, obtenemos todos los libros y recreamos los árboles
        # En una implementación más avanzada, se podría implementar la eliminación directa en el árbol
        libro = self.buscar_libro(id_libro)
        if not libro:
            print(f"Libro con ID {id_libro} no encontrado.")
            return False

        # Obtener todos los libros excepto el que queremos eliminar
        libros = [l for l in self.libros_por_id.inorder_traversal() if l.id_libro != id_libro]

        # Recrear los árboles
        self.libros_por_id = BinarySearchTree()
        self.libros_por_titulo = BinarySearchTree()

        # Reinsertar todos los libros excepto el eliminado
        for l in libros:
            self.libros_por_id.insert(l, lambda x: x.id_libro)
            self.libros_por_titulo.insert(l, lambda x: x.titulo.lower())

        print(f"Libro con ID {id_libro} eliminado.")
        return True

    def actualizar_libro(self, libro: Libro) -> bool:
        """Actualiza los datos de un libro existente.

        Args:
            libro (Libro): Objeto libro con los datos actualizados

        Returns:
            bool: True si el libro fue actualizado exitosamente, False si no se encontró
        """
        libro_existente = self.buscar_libro(libro.id_libro)
        if not libro_existente:
            print(f"Libro con ID {libro.id_libro} no se pudo encontrar para actualizar.")
            return False

        # Eliminar el libro actual y agregar la versión actualizada
        self.eliminar_libro(libro.id_libro)
        self.agregar_libro(libro)
        return True

    def buscar_libros(self, atributo: str, valor: str) -> List[Libro]:
        """Busca libros por coincidencia parcial en cualquier atributo.

        Args:
            atributo (str): Nombre del atributo a buscar (titulo, autor, categoria)
            valor (str): Valor a buscar en el atributo especificado

        Returns:
            List[Libro]: Lista de libros que coinciden con el criterio de búsqueda
        """
        valor = valor.lower()
        resultados = []

        # Usar el árbol más apropiado según el atributo de búsqueda
        if atributo == 'titulo':
            libros = self.libros_por_titulo.inorder_traversal()
        else:
            libros = self.libros_por_id.inorder_traversal()

        # Realizar la búsqueda
        for libro in libros:
            if atributo == 'titulo' and valor in libro.titulo.lower():
                resultados.append(libro)
            elif atributo == 'autor' and libro.autor and valor in libro.autor.lower():
                resultados.append(libro)
            elif atributo == 'categoria' and libro.categoria and valor in libro.categoria.lower():
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
        return self.libros_por_id.search(id_libro, lambda x: x.id_libro)

    def listar_libros(self) -> List[Libro]:
        """Retorna todos los libros ordenados por ID.

        Returns:
            List[Libro]: Lista ordenada de todos los libros
        """
        return self.libros_por_id.inorder_traversal()