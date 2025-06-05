class GrafoBiblioteca:
    def __init__(self):
        self.nodos = set()
        self.aristas = dict()  # (usuario_id, libro_id) -> datos

    def agregar_usuario(self, usuario_id):
        self.nodos.add(usuario_id)

    def agregar_libro(self, libro_id):
        self.nodos.add(libro_id)

    def prestar_libro(self, usuario_id, libro_id, datos=None):
        self.nodos.add(usuario_id)
        self.nodos.add(libro_id)
        self.aristas[(usuario_id, libro_id)] = datos or {}

    def devolver_libro(self, usuario_id, libro_id):
        self.aristas.pop((usuario_id, libro_id), None)

    def libros_prestados_por_usuario(self, usuario_id):
        return [libro for (usuario, libro) in self.aristas if usuario == usuario_id]

    def usuarios_que_prestaron_libro(self, libro_id):
        return [usuario for (usuario, libro) in self.aristas if libro == libro_id]

    def eliminar_usuario(self, usuario_id):
        self.nodos.discard(usuario_id)
        self.aristas = {k: v for k, v in self.aristas.items() if k[0] != usuario_id}

    def eliminar_libro(self, libro_id):
        self.nodos.discard(libro_id)
        self.aristas = {k: v for k, v in self.aristas.items() if k[1] != libro_id}