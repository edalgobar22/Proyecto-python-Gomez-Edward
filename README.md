# Clínica ACME

Aplicación de consola en Python para registrar usuarios, pacientes y consultas médicas, consultar la historia clínica, exportar prescripciones y generar un reporte anual de diagnósticos.

**Autor** Edward Gomez  
**Repositorio de entrega** `Proyecto_Python_GomezEdward`

## Cómo ejecutar

Abre una terminal en la carpeta del proyecto y ejecuta:

```powershell
python main.py
```

El proyecto usa Python 3 y su biblioteca estándar. En Windows también puedes usar `py -3 main.py` si tienes instalado el lanzador de Python.

### Cuenta de demostración

| Campo | Valor |
| --- | --- |
| Correo | `admin@acmeclinic.com` |
| Contraseña | `AcmeAdmin2026!` |

## Cómo probar la aplicación

1. Inicia sesión con la cuenta de demostración.
2. Registra un usuario con rol de médico y un paciente ficticio.
3. Cierra sesión con la opción `0` e ingresa con la cuenta del médico.
4. Selecciona la opción `3` y registra una consulta con fecha, síntomas, diagnóstico y medicamentos. Usa el formato `AAAA-MM-DD` para la fecha.
5. Selecciona la opción `4` y consulta la historia clínica por identificación del paciente.
6. Selecciona la opción `5` para generar el reporte anual. Presiona Enter para regresar al menú.

## Reporte anual de diagnósticos

La opción `5` agrupa todas las consultas guardadas por año. Muestra el total de diagnósticos, los médicos participantes registrados y los pacientes únicos. También calcula los promedios de síntomas y medicamentos por consulta, identifica el diagnóstico más frecuente y muestra las fechas de la primera y última consulta de cada año. La consola indica cuántas consultas se omitieron por fecha inválida.

El reporte aparece en consola y se guarda en `reporte_anual_diagnosticos.json`. Cada ejecución actualiza también `diagnosticos.json` y `usuarios.json`, que sirven como entradas del cálculo.

## Archivos del proyecto

| Archivo | Función |
| --- | --- |
| `main.py` | Punto de entrada de la aplicación. |
| `modulizacion.py` | Menú y flujo de inicio de sesión. |
| `personas.py` | Autenticación y registro de usuarios y pacientes. |
| `consultas.py` | Registro de consultas e historias clínicas. |
| `entradas.py` | Lectura y validación de texto, números y fechas. |
| `almacenamiento.py` | Lectura y escritura de datos, prescripciones e insumos del reporte. |
| `reportes.py` | Cálculo y exportación del reporte anual. |
| `datos.json` | Archivo requerido al iniciar. Guarda usuarios, pacientes y consultas. |
| `prescripcion_*.json` | Un archivo generado por cada consulta. La aplicación los regenera al iniciar. |
| `diagnosticos.json`, `usuarios.json`, `reporte_anual_diagnosticos.json` | Archivos generados por la opción `5`. |

## Entrega en GitHub

Crea un repositorio privado llamado `Proyecto_Python_GomezEdward`. Incluye el código, el README, el `.gitignore` y un `datos.json` con datos ficticios de demostración. La aplicación guarda contraseñas en texto plano, así que usa únicamente contraseñas de prueba. El `.gitignore` excluye cachés de Python, entornos virtuales y los JSON generados de prescripciones y reportes. Invita como colaboradores a las cuentas indicadas por el instructor y comparte el enlace del repositorio.
