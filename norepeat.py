import pandas as pd
import openpyxl

SHEET_NAME = "NOMBRE DE LA HORA"

df = pd.read_excel('./docs/input.xlsx', sheet_name=SHEET_NAME)

valuesAccept = []

# Ver el resultado del Excel
""" for row in df.itertuples():
    print(row) """

# Filtrar
for row in df.itertuples():
    if row.VALUE not in valuesAccept:
        valuesAccept.append(row.VALUE)

libro = openpyxl.Workbook()
hoja = libro.active

for fila in valuesAccept:
    hoja.append([fila])

libro.save("./docs/output.xlsx")

print('\n', valuesAccept)
print('\nLength: ', len(valuesAccept))
