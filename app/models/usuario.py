from datetime import datetime
from typing import List, Dict, Optional

class Usuario:
    """Clase para representar un usuario en el sistema de biblioteca.

    Esta clase maneja toda la información relacionada con los usuarios,
    incluyendo sus datos personales y el registro de sus préstamos.

    Attributes:
        id_usuario (int): Identificador único del usuario
        nombre (str): Nombre completo del usuario
        correo (str): Dirección de correo electrónico
        telefono (Optional[str]): Número de teléfono del usuario
        direccion (Optional[str]): Dirección física del usuario
        libros_prestados (List[int]): Lista de IDs de libros actualmente prestados
        historial_prestados (List[Dict]): Registro histórico de todos los préstamos
    """

    def __init__(self,
                 id_usuario: int,
                 nombre: str,
                 correo: str,
                 telefono: Optional[str] = None,
                 direccion: Optional[str] = None) -> None:

        """Inicializa los atributos del usuario.

        Args:
            id_usuario (int): Identificador único del usuario
            nombre (str): Nombre completo del usuario
            correo (str): Dirección de correo electrónico
            telefono (Optional[str], optional): Número de teléfono. Defaults to None
            direccion (Optional[str], optional): Dirección física. Defaults to None
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

        # Libros prestados actualmente
        self.libros_prestados: List[int] = []

        # Historial de préstamos
        self.historial_prestados: List[Dict[str, datetime]] = []

    def __str__(self) -> str:
        """Retorna una representación en string del usuario.

        Returns:
            str: Representación del usuario con sus atributos principales
        """
        return f"Usuario(ID: {self.id_usuario}, Nombre: {self.nombre}, Correo: {self.correo})"