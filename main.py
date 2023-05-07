import pandas as pd

df = pd.read_excel('./input.xlsx', sheet_name=1)

for row in df.itertuples():
    consulta_sql = "INSERT INTO \"general\".list_param (code, details, active) VALUES ('estrategia', '{\"code\": \"%s\", \"name\": \"%s\"}'::jsonb, true);\n" % (  # noqa: E501
        row.COD_SOLICITUD, row.Estrategias
    )

    print(consulta_sql)
