from almacenamiento import cargar_datos, exportar_prescripcion
from consultas import diagnosticar, historia_clinica
from personas import login, registrar_paciente, registrar_usuario
from reportes import reporte_anual_diagnosticos

def menu(datos, usuario):
    """Muestra las opciones disponibles tras iniciar sesión y ejecuta la opción seleccionada.

    Parámetros: datos (dict), estado de la clínica; usuario (dict), cuenta autenticada.
    Retorna: None al cerrar sesión con la opción 0. Las opciones se repiten hasta entonces.
    """
    opcion = ""
    while opcion != "0":
        print("\n1. Registrar usuario")
        print("2. Registrar paciente")
        print("3. Diagnosticar paciente (médicos)")
        print("4. Consultar historia clínica")
        print("5. Generar reporte anual de diagnósticos")
        print("0. Cerrar sesión")
        opcion = input("Opción: ")
        if opcion == "1":
            registrar_usuario(datos)
        elif opcion == "2":
            registrar_paciente(datos)
        elif opcion == "3":
            diagnosticar(datos, usuario)
        elif opcion == "4":
            historia_clinica(datos)
        elif opcion == "5":
            reporte_anual_diagnosticos()
        elif opcion != "0":
            print("Opción inválida.")


def iniciar():
    """Carga los datos, regenera las prescripciones guardadas y abre el inicio de sesión.

    Retorna: None cuando se elige salir desde el inicio de sesión.
    Tras cerrar una sesión en el menú, vuelve a pedir las credenciales.
    """
    datos = cargar_datos()
    # Regenera los archivos de prescripción desde las consultas guardadas.
    for consulta in datos["consultas"]:
        exportar_prescripcion(consulta)
    usuario = login(datos)
    while usuario != None:
        menu(datos, usuario)
        usuario = login(datos)
    print("Programa finalizado.")
