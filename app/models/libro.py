from datetime import datetime
from typing import List, Dict, Optional

class Libro:
    """Clase para representar un libro en el sistema de biblioteca.
    
    Esta clase maneja toda la información relacionada con los libros,
    incluyendo sus datos básicos, estado de préstamo, historial y valoraciones.
    
    Attributes:
        id_libro (int): Identificador único del libro
        titulo (str): Título del libro
        autor (Optional[str]): Nombre del autor del libro
        categoria (Optional[str]): Categoría o género del libro
        disponible (bool): Indica si el libro está disponible para préstamo
        fecha_prestamo (Optional[datetime]): Fecha cuando el libro fue prestado
        fecha_devolucion (Optional[datetime]): Fecha cuando debe ser devuelto
        historial_prestamos (List[Dict]): Registro de todos los préstamos del libro
        calificacion (float): Puntuación promedio del libro
        comentarios (List[str]): Lista de comentarios sobre el libro
    """

    def __init__(self,
                 id_libro: int,
                 titulo: str,
                 autor: Optional[str] = None,
                 categoria: Optional[str] = None) -> None:
        
        """Inicializa los atributos del libro.
        
        Args:
            id_libro (int): Identificador único del libro
            titulo (str): Título del libro
            autor (Optional[str], optional): Nombre del autor. Defaults to None
            categoria (Optional[str], optional): Categoría del libro. Defaults to None
        """
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor 
        self.categoria = categoria

        # Estado del libro
        self.disponible = True
        self.fecha_prestamo: Optional[datetime] = None
        self.fecha_devolucion: Optional[datetime] = None

        # Historial
        self.historial_prestamos: List[Dict[str, datetime]] = []

        # Valoraciones
        self.calificacion: float = 0.0
        self.comentarios: List[str] = []

    def __str__(self) -> str:
        """Retorna una representación en string del libro.
        
        Returns:
            str: Representación del libro con sus atributos principales
        """
        return f"Libro(ID: {self.id_libro}, Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria})"