
import json
from datetime import datetime
from collections import Counter
from almacenamiento import CARPETA
from almacenamiento import cargar_datos
from almacenamiento import exportar_datos_estadisticos


def reporte_anual_diagnosticos():

    # Actualizar los archivos JSON
    exportar_datos_estadisticos(cargar_datos())

    # Cargar diagnósticos
    with open(CARPETA / "diagnosticos.json", "r", encoding="utf-8") as archivo:
        diagnosticos = json.load(archivo)

    # Cargar usuarios
    with open(CARPETA / "usuarios.json", "r", encoding="utf-8") as archivo:
        usuarios = json.load(archivo)

    reporte = {"años": {}}
    diagnosticos_por_anio = {}
    invalidos = 0

    # Identificar los usuarios médicos
    medicos_registrados = set()

    for usuario in usuarios:
        if usuario["rol"] == "medico":
            medicos_registrados.add(usuario["identificacion"])

    # Agrupar diagnósticos por año
    for consulta in diagnosticos:

        try:
            fecha = datetime.strptime(
                consulta["fecha"], "%Y-%m-%d"
            )

            if fecha.date().isoformat() != consulta["fecha"]:
                raise ValueError("Fecha inválida")

        except (ValueError, KeyError, TypeError):
            invalidos += 1
            continue

        anio = consulta["fecha"][:4]

        if anio not in diagnosticos_por_anio:
            diagnosticos_por_anio[anio] = []

        diagnosticos_por_anio[anio].append(consulta)

    # Calcular estadísticas de cada año
    for anio, consultas in sorted(diagnosticos_por_anio.items()):

        total_diagnosticos = len(consultas)

        medicos = set()
        pacientes = set()

        total_sintomas = 0
        total_medicamentos = 0
        nombres_diagnosticos = []

        for consulta in consultas:

            # Médicos participantes
            id_medico = consulta["medico"]["identificacion"]

            if id_medico in medicos_registrados:
                medicos.add(id_medico)

            # Pacientes únicos
            pacientes.add(
                consulta["paciente"]["identificacion"]
            )

            # Contar síntomas
            sintomas = consulta["sintomas"]

            if isinstance(sintomas, str):
                sintomas = [
                    s.strip()
                    for s in sintomas.split(",")
                    if s.strip()
                ]

            total_sintomas += len(sintomas)

            # Contar medicamentos
            total_medicamentos += len(
                consulta["medicamentos"]
            )

            # Registrar nombre del diagnóstico
            nombres_diagnosticos.append(
                consulta["diagnostico"].strip().lower()
            )

        # Calcular promedios
        promedio_sintomas = round(
            total_sintomas / total_diagnosticos, 2
        )

        promedio_medicamentos = round(
            total_medicamentos / total_diagnosticos, 2
        )

        # Diagnóstico más común
        diagnostico_mas_comun = Counter(
            nombres_diagnosticos
        ).most_common(1)[0][0]

        # Primer y último diagnóstico
        primer_diagnostico = min(
            consultas, key=lambda consulta: consulta["fecha"]
        )

        ultimo_diagnostico = max(
            consultas, key=lambda consulta: consulta["fecha"]
        )

        # Guardar estadísticas del año
        reporte["años"][anio] = {
            "total_diagnosticos": total_diagnosticos,
            "medicos_participantes": len(medicos),
            "pacientes_atendidos": len(pacientes),
            "promedio_sintomas": promedio_sintomas,
            "promedio_medicamentos": promedio_medicamentos,
            "diagnostico_mas_comun": diagnostico_mas_comun.capitalize(),
            "primer_diagnostico": primer_diagnostico["fecha"],
            "ultimo_diagnostico": ultimo_diagnostico["fecha"]
        }

    # Generar archivo del reporte
    with open(
        CARPETA / "reporte_anual_diagnosticos.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            reporte,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    # Mostrar resultados en consola
    print("\n" + "=" * 55)
    print("       CLÍNICA ACME - REPORTE ANUAL")
    print("=" * 55)

    for anio, estadisticas in reporte["años"].items():

        print(f"\nAÑO: {anio}")
        print("-" * 55)

        for nombre, valor in estadisticas.items():

            nombre = nombre.replace("_", " ").capitalize()

            print(f"{nombre:30}: {valor}")

    if not reporte["años"]:
        print("No hay diagnósticos con fechas válidas.")

    print("\n" + "=" * 55)
    print(f"Diagnósticos con fecha inválida: {invalidos}")
    print("Reporte generado correctamente.")
    print("Archivo: reporte_anual_diagnosticos.json")
    print("=" * 55)

    input("\nPresiona ENTER para continuar...")
