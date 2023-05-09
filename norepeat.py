import pandas as pd
import openpyxl

SHEET_NAME = "SECTORES Y ACTIVIDAD"

df = pd.read_excel('./docs/input.xlsx', sheet_name=SHEET_NAME)

valuesAccept = []

# Ver el resultado del Excel
""" for row in df.itertuples():
    print(row) """

# Filtrar
for row in df.itertuples():
    if row.SECTOR not in valuesAccept:
        valuesAccept.append(row.SECTOR)


libro = openpyxl.Workbook()
hoja = libro.active

for fila in valuesAccept:
    hoja.append([fila])

libro.save("./docs/output.xlsx")

print('\n', valuesAccept)
print('\nCantidad de Datos:', len(valuesAccept))
