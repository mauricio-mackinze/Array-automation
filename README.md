# Automatizador de Suma de Matrices desde Excel

## Descripción

Este proyecto permite leer dos matrices almacenadas en un archivo Excel, realizar la suma de ambas y generar automáticamente un nuevo archivo Excel con el resultado.

El objetivo es demostrar el uso de Python para la automatización de tareas repetitivas relacionadas con el procesamiento de datos.

## Características

- Lectura de archivos Excel (.xlsx)
- Extracción automática de matrices
- Suma de matrices de igual dimensión
- Exportación del resultado a un nuevo archivo Excel
- Manejo básico de errores

## Tecnologías utilizadas

- Python 3
- Pandas
- OpenPyXL

## Instalación

```bash
pip install pandas openpyxl

---
Uso
Coloque el archivo matrices.xlsx en el mismo directorio del proyecto.
Ejecute:
python main.py
El programa generará un archivo llamado:
resultado.xlsx
Ejemplo

Matriz 1:

1	2
3	4

Matriz 2:

5	6
7	8

Resultado:

6	8
10	12

Autor
Mauricio Mackinze

# README (English)

```markdown
# Excel Matrix Addition Automation

## Description

This project reads two matrices stored in an Excel file, performs matrix addition, and automatically generates a new Excel file containing the result.

The purpose of this project is to demonstrate the use of Python for automating repetitive data-processing tasks.

## Features

- Read Excel files (.xlsx)
- Automatic matrix extraction
- Matrix addition
- Export results to a new Excel file
- Basic error handling

## Technologies

- Python 3
- Pandas
- OpenPyXL

## Installation

```bash
pip install pandas openpyxl
Usage
Place the file matrices.xlsx in the project directory.
Run:
python main.py
The program will generate:
resultado.xlsx
Example

Matrix 1:

1	2
3	4

Matrix 2:

5	6
7	8

Result:

6	8
10	12

Author
Mauricio Mackinze

## Real-World Applications

- Academic grade processing
- Inventory consolidation
- Financial reporting
- Spreadsheet automation
- Data entry reduction
