from typing import List, Optional
from app.models.usuario import Usuario

class UsuarioService:
    """Clase para gestionar las operaciones relacionadas con usuarios.

    Esta clase proporciona métodos para administrar el ciclo de vida de los usuarios,
    incluyendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y búsquedas.

    Attributes:
        usuarios (List[Usuario]): Lista de todos los usuarios registrados.
    """

    def __init__(self):
        """Inicializa la lista de usuarios del sistema."""
        self.usuarios: List[Usuario] = []

    def agregar_usuario(self, usuario: Usuario) -> bool:
        """Agrega un nuevo usuario al sistema.

        Args:
            usuario (Usuario): Objeto usuario a agregar.

        Returns:
            bool: True si el usuario fue agregado exitosamente, False si ya existe.
        """
        if self.buscar_usuario(usuario.id_usuario):
            print(f"Usuario con ID {usuario.id_usuario} ya existe.")
            return False
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} (ID: {usuario.id_usuario}) agregado correctamente.")
        return True

    def eliminar_usuario(self, id_usuario: int) -> bool:
        """Elimina un usuario del sistema.

        Args:
            id_usuario (int): ID del usuario a eliminar.

        Returns:
            bool: True si el usuario fue eliminado exitosamente, False si no se encontró.
        """
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            if usuario.libros_prestados:
                print(f"No se puede eliminar el usuario {id_usuario} porque tiene libros prestados.")
                return False
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado correctamente.")
            return True
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return False

    def actualizar_usuario(self, usuario: Usuario) -> bool:
        """Actualiza los datos de un usuario existente.

        Args:
            usuario (Usuario): Objeto usuario con los datos actualizados.

        Returns:
            bool: True si el usuario fue actualizado exitosamente, False si no se encontró.
        """
        usuario_existente = self.buscar_usuario(usuario.id_usuario)
        if usuario_existente:
            usuario_existente.nombre = usuario.nombre
            usuario_existente.correo = usuario.correo
            return True
        print(f"Usuario con ID {usuario.id_usuario} no encontrado para actualizar.")
        return False

    def buscar_usuario(self, id_usuario: int) -> Optional[Usuario]:
        """Busca un usuario específico por su ID.

        Args:
            id_usuario (int): ID del usuario a buscar.

        Returns:
            Optional[Usuario]: El usuario encontrado o None si no existe.
        """
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def buscar_usuarios(self, atributo: str, valor: str) -> List[Usuario]:
        """Busca usuarios por coincidencia parcial en cualquier atributo.

        Args:
            atributo (str): Nombre del atributo a buscar (nombre, correo, etc.).
            valor (str): Valor a buscar en el atributo especificado.

        Returns:
            List[Usuario]: Lista de usuarios que coinciden con el criterio de búsqueda.
        """
        resultados = []
        for usuario in self.usuarios:
            if hasattr(usuario, atributo):
                valor_usuario = getattr(usuario, atributo)
                if valor.lower() in str(valor_usuario).lower():
                    resultados.append(usuario)

        if not resultados:
            print(f"No se encontraron usuarios con {atributo} que contenga '{valor}'.")
        return resultados