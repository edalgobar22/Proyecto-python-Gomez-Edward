from almacenamiento import guardar_datos
from entradas import pedir_texto


def buscar_persona(personas, identificacion):
    """Busca la primera persona que coincide con la identificación indicada.

    Parámetros: personas (list), lista de diccionarios; identificacion (str), valor exacto que se busca.
    Retorna: El diccionario de la persona encontrada o None si no hay coincidencias.
    """
    for persona in personas:
        if persona["identificacion"] == identificacion:
            return persona
    return None


def login(datos):
    """Pide correo y contraseña hasta autenticar al usuario o recibir la opción 0.

    Parámetros: datos (dict), del que se consulta la lista de usuarios.
    Retorna: El diccionario del usuario autenticado o None si elige salir.
    Convierte el correo a minúsculas y compara la contraseña tal como se guarda.
    """
    while True:
        print("\nINICIO DE SESIÓN")
        correo = pedir_texto("Correo (0 para salir): ").lower()
        if correo == "0":
            return None
        clave = pedir_texto("Contraseña (visible): ")
        for usuario in datos["usuarios"]:
            if usuario["email"] == correo and usuario["contrasena"] == clave:
                return usuario
        print("Correo o contraseña incorrectos.")


def pedir_persona(personas):
    """Solicita identificación, nombres, apellidos, teléfono, correo y dirección.

    Parámetros: personas (list), registros donde se comprueba si la identificación ya existe.
    Retorna: Un diccionario con los datos básicos o None si la identificación está repetida.
    Guarda la identificación como texto y aplica una comprobación básica al correo.
    """
    identificacion = pedir_texto("Identificación: ")
    if buscar_persona(personas, identificacion) != None:
        print("Esta identificación ya está registrada.")
        return None
    nombres = pedir_texto("Nombres: ")
    apellidos = pedir_texto("Apellidos: ")
    telefono = pedir_texto("Teléfono: ")
    correo = pedir_texto("Email: ").lower()
    while correo.count("@") != 1 or correo.startswith("@") or correo.endswith("@") or " " in correo:
        print("Escribe un correo válido.")
        correo = pedir_texto("Email: ").lower()
    direccion = pedir_texto("Dirección: ")
    return {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": correo,
        "direccion": direccion
    }


def registrar_usuario(datos):
    """Registra por consola un médico o un administrativo.

    Parámetros: datos (dict), estado actual de la clínica.
    Retorna: None. Cancela el registro si la identificación o el correo ya existen.
    Si se completa, agrega el usuario a la lista y guarda los datos en el JSON.
    Solicita confirmar la contraseña y la almacena como texto en esta versión de clase.
    """
    usuario = pedir_persona(datos["usuarios"])
    if usuario == None:
        return
    for registrado in datos["usuarios"]:
        if registrado["email"] == usuario["email"]:
            print("Este correo ya está registrado.")
            return
    rol = pedir_texto("Rol (1. Médico / 2. Administrativo): ")
    while rol != "1" and rol != "2":
        rol = pedir_texto("Selecciona 1 o 2: ")
    if rol == "1":
        usuario["rol"] = "medico"
    else:
        usuario["rol"] = "administrativo"
    clave = pedir_texto("Contraseña asignada (visible): ")
    confirmacion = pedir_texto("Repite la contraseña: ")
    while clave != confirmacion:
        print("Las contraseñas no coinciden.")
        clave = pedir_texto("Contraseña asignada: ")
        confirmacion = pedir_texto("Repite la contraseña: ")
    usuario["contrasena"] = clave
    datos["usuarios"].append(usuario)
    guardar_datos(datos)
    print("Usuario registrado.")


def registrar_paciente(datos):
    """Registra los datos básicos, el género y el estado civil de un paciente.

    Parámetros: datos (dict), estado actual de la clínica.
    Retorna: None. Si la identificación ya existe, cancela el registro.
    Si se completa, agrega el paciente a la lista y guarda los datos en el JSON.
    """
    paciente = pedir_persona(datos["pacientes"])
    if paciente == None:
        return
    paciente["genero"] = pedir_texto("Género: ")
    paciente["estado_civil"] = pedir_texto("Estado civil: ")
    datos["pacientes"].append(paciente)
    guardar_datos(datos)
    print("Paciente registrado.")
