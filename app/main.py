from typing import List, Dict, Optional
from app.services.libro_service import LibroService
from app.services.usuarioservice import UsuarioService
from app.services.prestamos_services import PrestamoService
from app.models.libro import Libro
from app.models.usuario import Usuario

def menu_principal():
    """Muestra el menú principal."""
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Gestión de Libros")
    print("2. Gestión de Usuarios")
    print("3. Préstamos y Devoluciones")
    print("4. Salir")

def menu_libros():
    """Muestra el menú de gestión de libros."""
    print("\n--- Gestión de Libros ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Actualizar libro")
    print("4. Buscar libros")
    print("5. Listar todos los libros")
    print("6. Volver al menú principal")

def mostrar_menu_ordenamiento():
    """Muestra las opciones de ordenamiento."""
    print("\nOrdenar libros por:")
    print("1. ID")
    print("2. Título")
    print("3. Autor")
    print("4. Categoría")
    print("5. Disponibilidad")

def ordenar_libros(libros: List[Libro], criterio: str) -> List[Libro]:
    """
    Ordena la lista de libros según el criterio especificado.

    Args:
        libros: Lista de libros a ordenar
        criterio: Criterio de ordenamiento ('id', 'titulo', 'autor', 'categoria', 'disponible')

    Returns:
        Lista ordenada de libros
    """
    if criterio == 'id':
        return sorted(libros, key=lambda x: x.id_libro)
    elif criterio == 'titulo':
        return sorted(libros, key=lambda x: x.titulo.lower())
    elif criterio == 'autor':
        return sorted(libros, key=lambda x: (x.autor or '').lower())
    elif criterio == 'categoria':
        return sorted(libros, key=lambda x: (x.categoria or '').lower())
    elif criterio == 'disponible':
        return sorted(libros, key=lambda x: x.disponible, reverse=True)
    return libros

def mostrar_libros(libros: List[Libro]):
    """
    Muestra la lista de libros en formato tabular.

    Args:
        libros: Lista de libros a mostrar
    """
    if not libros:
        print("\nNo hay libros registrados en el sistema.")
        return

    # Definir el formato de la tabla
    print("\n{:<5} {:<30} {:<20} {:<15} {:<12}".format(
        "ID", "Título", "Autor", "Categoría", "Disponible"))
    print("-" * 85)

    # Mostrar cada libro
    for libro in libros:
        disponible = "Sí" if libro.disponible else "No"
        print("{:<5} {:<30} {:<20} {:<15} {:<12}".format(
            libro.id_libro,
            libro.titulo[:27] + "..." if len(libro.titulo) > 27 else libro.titulo,
            libro.autor[:17] + "..." if len(libro.autor) > 17 else libro.autor,
            libro.categoria[:12] + "..." if len(libro.categoria) > 12 else libro.categoria,
            disponible
        ))

def menu_usuarios():
    """Muestra el menú de gestión de usuarios."""
    print("\n--- Gestión de Usuarios ---")
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Actualizar usuario")
    print("4. Buscar usuarios")
    print("5. Volver al menú principal")

def menu_prestamos():
    """Muestra el menú de préstamos y devoluciones."""
    print("\n--- Préstamos y Devoluciones ---")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Volver al menú principal")

def solicitar_entero(mensaje: str) -> int:
    """Solicita un número entero al usuario con validación."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    """Función principal del programa."""
    # Inicializar servicios
    libro_service = LibroService()
    usuario_service = UsuarioService()
    prestamo_service = PrestamoService()

    while True:
        menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":  # Gestión de Libros
            while True:
                menu_libros()
                opcion_libros = input("Selecciona una opción: ")

                if opcion_libros == "1":  # Agregar libro
                    id_libro = solicitar_entero("ID del libro: ")
                    titulo = input("Título del libro: ")
                    autor = input("Autor del libro: ")
                    categoria = input("Categoría del libro: ")
                    libro = Libro(id_libro, titulo, autor, categoria)
                    libro_service.agregar_libro(libro)

                elif opcion_libros == "2":  # Eliminar libro
                    id_libro = solicitar_entero("ID del libro a eliminar: ")
                    libro_service.eliminar_libro(id_libro)

                elif opcion_libros == "3":  # Actualizar libro
                    id_libro = solicitar_entero("ID del libro a actualizar: ")
                    titulo = input("Nuevo título del libro: ")
                    autor = input("Nuevo autor del libro: ")
                    categoria = input("Nueva categoría del libro: ")
                    libro = Libro(id_libro, titulo, autor, categoria)
                    libro_service.actualizar_libro(libro)

                elif opcion_libros == "4":  # Buscar libros
                    atributo = input("Atributo para buscar (titulo, autor, categoria): ")
                    valor = input(f"Valor a buscar en {atributo}: ")
                    resultados = libro_service.buscar_libros(atributo, valor)
                    if resultados:
                        mostrar_libros(resultados)
                    else:
                        print(f"No se encontraron libros con {atributo} que contenga '{valor}'.")

                elif opcion_libros == "5":  # Listar todos los libros
                    if not libro_service.libros:
                        print("\nNo hay libros registrados en el sistema.")
                        continue

                    mostrar_menu_ordenamiento()
                    opcion_orden = input("Selecciona una opción de ordenamiento: ")

                    criterio = {
                        "1": "id",
                        "2": "titulo",
                        "3": "autor",
                        "4": "categoria",
                        "5": "disponible"
                    }.get(opcion_orden)

                    if criterio:
                        libros_ordenados = ordenar_libros(libro_service.libros, criterio)
                        mostrar_libros(libros_ordenados)
                    else:
                        print("Opción de ordenamiento no válida.")

                elif opcion_libros == "6":  # Volver al menú principal
                    break

        elif opcion == "2":  # Gestión de Usuarios
            while True:
                menu_usuarios()
                opcion_usuarios = input("Selecciona una opción: ")

                if opcion_usuarios == "1":  # Agregar usuario
                    id_usuario = solicitar_entero("ID del usuario: ")
                    nombre = input("Nombre del usuario: ")
                    correo = input("Correo del usuario: ")
                    usuario = Usuario(id_usuario, nombre, correo)
                    usuario_service.agregar_usuario(usuario)

                elif opcion_usuarios == "2":  # Eliminar usuario
                    id_usuario = solicitar_entero("ID del usuario a eliminar: ")
                    usuario_service.eliminar_usuario(id_usuario)

                elif opcion_usuarios == "3":  # Actualizar usuario
                    id_usuario = solicitar_entero("ID del usuario a actualizar: ")
                    nombre = input("Nuevo nombre del usuario: ")
                    correo = input("Nuevo correo del usuario: ")
                    usuario = Usuario(id_usuario, nombre, correo)
                    usuario_service.actualizar_usuario(usuario)

                elif opcion_usuarios == "4":  # Buscar usuarios
                    atributo = input("Atributo para buscar (nombre, correo): ")
                    valor = input(f"Valor a buscar en {atributo}: ")
                    resultados = usuario_service.buscar_usuarios(atributo, valor)
                    if resultados:
                        for usuario in resultados:
                            print(usuario)
                    else:
                        print(f"No se encontraron usuarios con {atributo} que contenga '{valor}'.")

                elif opcion_usuarios == "5":  # Volver al menú principal
                    break

        elif opcion == "3":  # Préstamos y Devoluciones
            while True:
                menu_prestamos()
                opcion_prestamos = input("Selecciona una opción: ")

                if opcion_prestamos == "1":  # Prestar libro
                    id_libro = solicitar_entero("ID del libro a prestar: ")
                    id_usuario = solicitar_entero("ID del usuario que solicita el préstamo: ")
                    libro = libro_service.buscar_libro(id_libro)
                    usuario = usuario_service.buscar_usuario(id_usuario)
                    if libro and usuario:
                        prestamo_service.prestar_libro(libro, usuario)
                    else:
                        print("Libro o usuario no encontrado.")

                elif opcion_prestamos == "2":  # Devolver libro
                    id_libro = solicitar_entero("ID del libro a devolver: ")
                    id_usuario = solicitar_entero("ID del usuario que devuelve el libro: ")
                    libro = libro_service.buscar_libro(id_libro)
                    usuario = usuario_service.buscar_usuario(id_usuario)
                    if libro and usuario:
                        prestamo_service.devolver_libro(libro, usuario)
                    else:
                        print("Libro o usuario no encontrado.")

                elif opcion_prestamos == "3":  # Volver al menú principal
                    break

        elif opcion == "4":  # Salir
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()