import json
from pathlib import Path


CARPETA = Path(__file__).resolve().parent
RUTA_DATOS = CARPETA / "datos.json"


def cargar_datos():
    """Lee el archivo JSON de la clínica indicado por la constante RUTA_DATOS.

    Retorna: Un diccionario con las listas de usuarios, pacientes y consultas.
    Puede producir un error si el archivo no existe o el JSON no es válido.
    """
    with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos


def guardar_datos(datos):
    """Sobrescribe el archivo de datos con el estado actual de la clínica.

    Parámetros: datos (dict), con las listas de usuarios, pacientes y consultas.
    Retorna: None. Guarda el JSON con sangría y conserva las tildes.
    """
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def exportar_prescripcion(consulta):
    """Escribe la consulta completa en un archivo JSON en la carpeta del proyecto.

    Parámetros: consulta (dict), con su número, fecha, paciente, médico y datos clínicos.
    Retorna: El nombre del archivo, por ejemplo prescripcion_1.json.
    Si existe un archivo con ese número, lo sobrescribe.
    """
    nombre = "prescripcion_" + str(consulta["numero"]) + ".json"
    with open(CARPETA / nombre, "w", encoding="utf-8") as archivo:
        json.dump(consulta, archivo, indent=4, ensure_ascii=False)
    return nombre
