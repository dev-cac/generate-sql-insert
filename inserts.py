import pandas as pd

SHEET_NAME = "NOMBRE DE LA HOJA"

df = pd.read_excel('./docs/input.xlsx', sheet_name=SHEET_NAME)

# Ver el resultado del Excel
""" for row in df.itertuples():
    print(row) """


# Crear los inserts
for row in df.itertuples():
    consulta_sql = "INSERT INTO \"general\".list_param (code, details, active) VALUES ('tipo', '{\"code\": \"%s\", \"name\": \"%s\"}'::jsonb, true);\n" % (  # noqa: E501
        row.COL1,
        row.COL2
    )

    print(consulta_sql)
