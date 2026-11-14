def pedir_texto(mensaje):
    """Solicita un texto obligatorio en la consola.

    Parámetros: mensaje (str), pregunta que se muestra al usuario.
    Retorna: El texto sin espacios al inicio ni al final. Si queda vacío, vuelve a pedirlo.
    """
    texto = input(mensaje).strip()
    while texto == "":
        print("Este dato es obligatorio.")
        texto = input(mensaje).strip()
    return texto


def pedir_numero(mensaje):
    """Solicita un número entero mayor que cero en la consola.

    Parámetros: mensaje (str), pregunta que se muestra al usuario.
    Retorna: El entero ingresado. Repite la solicitud si el valor no es válido.
    """
    texto = pedir_texto(mensaje)
    while not texto.isdecimal() or int(texto) <= 0:
        print("Escribe un entero mayor que cero.")
        texto = pedir_texto(mensaje)
    return int(texto)


def pedir_fecha():
    """Pide el día, mes y año de la consulta por separado.

    Valida el año de cuatro cifras, el mes y los días que admite, incluyendo años bisiestos.
    Retorna: La fecha como texto en formato AAAA-MM-DD, por ejemplo 2026-11-12.
    """
    # Se ingresa la fecha manualmente.
    dia = pedir_numero("Día de la consulta: ")
    mes = pedir_numero("Mes de la consulta: ")
    anio = pedir_numero("Año de la consulta (cuatro cifras): ")
    while anio < 1000 or anio > 9999:
        anio = pedir_numero("Escribe un año de cuatro cifras: ")
    while mes > 12:
        mes = pedir_numero("Mes entre 1 y 12: ")
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
        dias_mes[1] = 29
    while dia > dias_mes[mes - 1]:
        dia = pedir_numero("Día válido para ese mes: ")
    return f"{anio:04d}-{mes:02d}-{dia:02d}"
