from datetime import datetime, timedelta
from typing import List, Dict
from app.models.libro import Libro
from app.models.usuario import Usuario

class PrestamoService:
    """Clase para gestionar los préstamos y devoluciones de libros.

    Esta clase proporciona métodos para realizar préstamos, registrar devoluciones,
    consultar préstamos actuales y verificar retrasos.

    Methods:
        prestar_libro: Realiza el préstamo de un libro a un usuario.
        devolver_libro: Registra la devolución de un libro.
        consultar_prestamos_actuales: Consulta los libros actualmente prestados a un usuario.
        consultar_historial_prestamos: Consulta el historial completo de préstamos de un usuario.
        verificar_retrasos: Verifica si un usuario tiene libros con retraso en la devolución.
    """

    def prestar_libro(self, libro: Libro, usuario: Usuario) -> bool:
        """Realiza el préstamo de un libro a un usuario.

        Args:
            libro (Libro): El libro a prestar.
            usuario (Usuario): El usuario que solicita el préstamo.

        Returns:
            bool: True si el préstamo fue exitoso, False en caso contrario.
        """
        if not libro.disponible:
            print(f"El libro '{libro.titulo}' no está disponible.")
            return False

        if len(usuario.libros_prestados) >= 3:
            print(f"El usuario {usuario.nombre} ya tiene el máximo de libros permitidos.")
            return False

        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=15)

        libro.disponible = False
        libro.fecha_prestamo = fecha_prestamo
        libro.fecha_devolucion = fecha_devolucion

        prestamo_libro = {
            'id_usuario': usuario.id_usuario,
            'fecha_prestamo': fecha_prestamo,
            'fecha_devolucion_esperada': fecha_devolucion
        }
        libro.historial_prestamos.append(prestamo_libro)

        usuario.libros_prestados.append(libro.id_libro)
        prestamo_usuario = {
            'id_libro': libro.id_libro,
            'fecha_prestamo': fecha_prestamo,
            'fecha_devolucion_esperada': fecha_devolucion
        }
        usuario.historial_prestados.append(prestamo_usuario)

        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre} exitosamente.")
        print(f"Fecha de devolución esperada: {fecha_devolucion.strftime('%Y-%m-%d')}")
        return True

    def devolver_libro(self, libro: Libro, usuario: Usuario) -> bool:
        """Registra la devolución de un libro.

        Args:
            libro (Libro): El libro a devolver.
            usuario (Usuario): El usuario que devuelve el libro.

        Returns:
            bool: True si la devolución fue exitosa, False en caso contrario.
        """
        if libro.id_libro not in usuario.libros_prestados:
            print(f"El libro '{libro.titulo}' no está prestado a {usuario.nombre}.")
            return False

        fecha_devolucion = datetime.now()

        libro.disponible = True
        libro.fecha_prestamo = None
        libro.fecha_devolucion = None

        if libro.historial_prestamos:
            ultimo_prestamo = libro.historial_prestamos[-1]
            ultimo_prestamo['fecha_devolucion_real'] = fecha_devolucion

            dias_retraso = (fecha_devolucion - ultimo_prestamo['fecha_devolucion_esperada']).days
            if dias_retraso > 0:
                ultimo_prestamo['dias_retraso'] = dias_retraso
                print(f"¡Atención! El libro fue devuelto con {dias_retraso} días de retraso.")

        usuario.libros_prestados.remove(libro.id_libro)

        for prestamo in usuario.historial_prestados:
            if prestamo['id_libro'] == libro.id_libro and 'fecha_devolucion_real' not in prestamo:
                prestamo['fecha_devolucion_real'] = fecha_devolucion
                break

        print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre} exitosamente.")
        return True

    def consultar_prestamos_actuales(self, usuario: Usuario) -> List[int]:
        """Consulta los libros actualmente prestados a un usuario.

        Args:
            usuario (Usuario): El usuario a consultar.

        Returns:
            List[int]: Lista de IDs de libros prestados.
        """
        return usuario.libros_prestados

    def consultar_historial_prestamos(self, usuario: Usuario) -> List[Dict]:
        """Consulta el historial completo de préstamos de un usuario.

        Args:
            usuario (Usuario): El usuario a consultar.

        Returns:
            List[Dict]: Lista de préstamos históricos.
        """
        return usuario.historial_prestados

    def verificar_retrasos(self, usuario: Usuario) -> List[Dict]:
        """Verifica si un usuario tiene libros con retraso en la devolución.

        Args:
            usuario (Usuario): El usuario a verificar.

        Returns:
            List[Dict]: Lista de préstamos con retraso.
        """
        retrasos = []
        fecha_actual = datetime.now()

        for prestamo in usuario.historial_prestados:
            if 'fecha_devolucion_real' not in prestamo:
                dias_retraso = (fecha_actual - prestamo['fecha_devolucion_esperada']).days
                if dias_retraso > 0:
                    retrasos.append({
                        'id_libro': prestamo['id_libro'],
                        'dias_retraso': dias_retraso
                    })

        return retrasos