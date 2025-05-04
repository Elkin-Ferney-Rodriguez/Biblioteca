from typing import List, Optional
from app.models.usuario import Usuario
from app.structures.binary_search_tree import BinarySearchTree

class UsuarioService:
    """Clase para gestionar las operaciones relacionadas con usuarios."""

    def __init__(self):
        self.usuarios_por_id = BinarySearchTree()
        self.usuarios_por_nombre = BinarySearchTree()

    def agregar_usuario(self, usuario: Usuario) -> bool:
        if self.usuarios_por_id.insert(usuario, lambda x: x.id_usuario):
            self.usuarios_por_nombre.insert(usuario, lambda x: x.nombre.lower())
            print(f"Usuario {usuario.nombre} (ID: {usuario.id_usuario}) agregado correctamente.")
            return True
        print(f"Usuario con ID {usuario.id_usuario} ya existe.")
        return False

    def eliminar_usuario(self, id_usuario: int) -> bool:
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return False
        if usuario.libros_prestados:
            print(f"No se puede eliminar el usuario {id_usuario} porque tiene libros prestados.")
            return False

        # Recrear los árboles sin el usuario eliminado
        usuarios = [u for u in self.usuarios_por_id.inorder_traversal() if u.id_usuario != id_usuario]
        self.usuarios_por_id = BinarySearchTree()
        self.usuarios_por_nombre = BinarySearchTree()
        for u in usuarios:
            self.usuarios_por_id.insert(u, lambda x: x.id_usuario)
            self.usuarios_por_nombre.insert(u, lambda x: x.nombre.lower())
        print(f"Usuario con ID {id_usuario} eliminado correctamente.")
        return True

    def actualizar_usuario(self, usuario: Usuario) -> bool:
        usuario_existente = self.buscar_usuario(usuario.id_usuario)
        if not usuario_existente:
            print(f"Usuario con ID {usuario.id_usuario} no encontrado para actualizar.")
            return False
        self.eliminar_usuario(usuario.id_usuario)
        self.agregar_usuario(usuario)
        return True

    def buscar_usuario(self, id_usuario: int) -> Optional[Usuario]:
        return self.usuarios_por_id.search(id_usuario, lambda x: x.id_usuario)

    def buscar_usuarios(self, atributo: str, valor: str) -> List[Usuario]:
        valor = valor.lower()
        if atributo == 'nombre':
            usuarios = self.usuarios_por_nombre.inorder_traversal()
        else:
            usuarios = self.usuarios_por_id.inorder_traversal()
        resultados = []
        for usuario in usuarios:
            if atributo == 'nombre' and valor in usuario.nombre.lower():
                resultados.append(usuario)
            elif atributo == 'correo' and valor in usuario.correo.lower():
                resultados.append(usuario)
        if not resultados:
            print(f"No se encontraron usuarios con {atributo} que contenga '{valor}'.")
        return resultados

    def listar_usuarios(self) -> List[Usuario]:
        return self.usuarios_por_id.inorder_traversal()