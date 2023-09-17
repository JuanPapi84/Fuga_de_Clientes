# Obtener los días totales de servicio, creando primero una columna que se llame `TotalService`
df['TotalService'] = df['EndDate']
# Reemplazar nan con fecha 2020-02-01
df['TotalService'] = df['TotalService'].fillna(pd.to_datetime('2020-02-01'))
# Extración de los días
df['Days'] = (df['TotalService'] - df['BeginDate']).dt.days
# Extración y creación de la columna años
df['BeginYear'] = df['BeginDate'].dt.year