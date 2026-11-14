# Clínica ACME

Aplicación de consola en Python para registrar usuarios, pacientes y consultas médicas. Permite consultar la historia clínica de un paciente y exporta una prescripción en JSON por cada consulta.

**Autor:** Edward Gomez  
**Repositorio de entrega:** `Proyecto_Python_GomezEdward`

## Cómo ejecutar

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python main.py
```

El proyecto usa Python 3 y su biblioteca estándar. Si tu instalación usa el comando `python3` o `python3.15`, reemplaza `python` por ese comando.

### Cuenta de demostración

- Correo: `admin@acmeclinic.com`
- Contraseña: `AcmeAdmin2026!`

## Cómo probar la aplicación

1. Inicia sesión con la cuenta de demostración.
2. Registra un usuario con el rol de médico y registra un paciente ficticio.
3. Cierra sesión con la opción `0` e ingresa con la cuenta del médico.
4. Registra una consulta con fecha, síntomas, diagnóstico y medicamentos.
5. Consulta la historia clínica usando la identificación del paciente.

La aplicación guarda los registros en `datos.json` y genera archivos como `prescripcion_1.json` junto al código. Usa únicamente datos ficticios y contraseñas de prueba, ya que esta versión de clase guarda las contraseñas en texto plano.

## Archivos

| Archivo | Función |
| --- | --- |
| `main.py` | Punto de entrada de la aplicación. |
| `modulizacion.py` | Menú y flujo de inicio de sesión. |
| `personas.py` | Autenticación y registro de usuarios y pacientes. |
| `consultas.py` | Registro de consultas e historias clínicas. |
| `entradas.py` | Lectura y validación de texto, números y fechas. |
| `almacenamiento.py` | Lectura y escritura de datos y prescripciones JSON. |
| `datos.json` | Datos iniciales y registros guardados. |
| `.gitignore` | Exclusión de cachés, entornos virtuales y prescripciones generadas. |

## Entrega en GitHub

Crea un repositorio privado llamado `Proyecto_Python_GomezEdward`. Sube el contenido de esta carpeta, incluido `.gitignore`. Conserva `datos.json` con los datos de demostración en la versión que entregues. Invita como colaboradores a las cuentas indicadas por el instructor y comparte el enlace del repositorio.
