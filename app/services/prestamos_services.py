from datetime import datetime, timedelta
from typing import List, Dict
from app.models.libro import Libro
from app.models.usuario import Usuario
from app.structures.grafo_biblioteca import GrafoBiblioteca

class PrestamoService:
    """Clase para gestionar los préstamos y devoluciones de libros."""

    def __init__(self):
        self.grafo = GrafoBiblioteca()

    def prestar_libro(self, libro: Libro, usuario: Usuario) -> bool:
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

        # --- Actualiza el grafo ---
        self.grafo.prestar_libro(
            usuario.id_usuario,
            libro.id_libro,
            {
                'fecha_prestamo': fecha_prestamo,
                'fecha_devolucion_esperada': fecha_devolucion
            }
        )

        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre} exitosamente.")
        print(f"Fecha de devolución esperada: {fecha_devolucion.strftime('%Y-%m-%d')}")
        return True

    def devolver_libro(self, libro: Libro, usuario: Usuario) -> bool:
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

        # --- Actualiza el grafo ---
        self.grafo.devolver_libro(usuario.id_usuario, libro.id_libro)

        print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre} exitosamente.")
        return True

    def consultar_prestamos_actuales(self, usuario: Usuario) -> List[int]:
        return usuario.libros_prestados

    def consultar_historial_prestamos(self, usuario: Usuario) -> List[Dict]:
        return usuario.historial_prestados

    def verificar_retrasos(self, usuario: Usuario) -> List[Dict]:
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