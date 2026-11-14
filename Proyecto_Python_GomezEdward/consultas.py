from almacenamiento import exportar_prescripcion, guardar_datos
from entradas import pedir_fecha, pedir_numero, pedir_texto
from personas import buscar_persona


def diagnosticar(datos, medico):
    """Registra los síntomas, el diagnóstico y uno o más medicamentos de una consulta.

    Parámetros: datos (dict), estado de la clínica; medico (dict), usuario que inició sesión.
    Retorna: None. Solo registra la consulta si el usuario es médico y el paciente existe.
    Agrega la consulta a la lista, guarda el estado en datos.json y exporta la prescripción.
    """
    if medico["rol"] != "medico":
        print("Inicia sesión con un usuario médico para registrar el diagnóstico.")
        return
    identificacion = pedir_texto("Identificación del paciente: ")
    paciente = buscar_persona(datos["pacientes"], identificacion)
    if paciente == None:
        print("Primero debes registrar al paciente.")
        return
    fecha = pedir_fecha()
    sintomas = pedir_texto("Síntomas: ")
    diagnostico = pedir_texto("Diagnóstico: ")
    medicamentos = []
    agregar = "s"
    while agregar == "s":
        medicamento = {
            "medicamento": pedir_texto("Medicamento: "),
            "cantidad": pedir_numero("Cantidad total: "),
            "dosis_diaria": pedir_texto("Dosis diaria (incluye unidades): "),
            "dias_tratamiento": pedir_numero("Días de tratamiento: ")
        }
        medicamentos.append(medicamento)
        agregar = pedir_texto("¿Agregar otro medicamento? (s/n): ").lower()
        while agregar != "s" and agregar != "n":
            agregar = pedir_texto("Escribe s o n: ").lower()
    consulta = {
        "numero": len(datos["consultas"]) + 1,
        "fecha": fecha,
        "paciente": paciente,
        "medico": {
            "identificacion": medico["identificacion"],
            "nombres": medico["nombres"],
            "apellidos": medico["apellidos"],
            "email": medico["email"]
        },
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "medicamentos": medicamentos
    }
    datos["consultas"].append(consulta)
    guardar_datos(datos)
    nombre = exportar_prescripcion(consulta)
    print("Consulta registrada. Prescripción guardada en", nombre)


def historia_clinica(datos):
    """Muestra en consola la ficha y las consultas de un paciente buscado por identificación.

    Parámetros: datos (dict), con las listas de pacientes y consultas.
    Retorna: None. Si falta la ficha o no hay consultas, muestra el mensaje correspondiente.
    Imprime la fecha, el médico, los síntomas, el diagnóstico y los medicamentos de cada consulta.
    """
    identificacion = pedir_texto("Identificación del paciente: ")
    paciente = buscar_persona(datos["pacientes"], identificacion)
    if paciente == None:
        print("Paciente no registrado.")
        return
    print("\nHISTORIA CLÍNICA")
    for campo in paciente:
        print(campo, ":", paciente[campo])
    cantidad = 0
    for consulta in datos["consultas"]:
        if consulta["paciente"]["identificacion"] == identificacion:
            cantidad += 1
            print("\nFecha:", consulta["fecha"])
            print("Médico:", consulta["medico"]["nombres"], consulta["medico"]["apellidos"])
            print("Identificación del médico:", consulta["medico"]["identificacion"])
            print("Síntomas:", consulta["sintomas"])
            print("Diagnóstico:", consulta["diagnostico"])
            for medicamento in consulta["medicamentos"]:
                print("Medicamento:", medicamento["medicamento"])
                print("Cantidad:", medicamento["cantidad"])
                print("Dosis diaria:", medicamento["dosis_diaria"])
                print("Días de tratamiento:", medicamento["dias_tratamiento"])
    if cantidad == 0:
        print("El paciente todavía no tiene consultas.")
