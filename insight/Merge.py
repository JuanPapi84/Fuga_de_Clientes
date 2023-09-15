# Fusionar DataFrames utilizando pd.merge() con unión externa

df = df_contratos.merge(df_internet, on="customerID", how="left")
df = df.merge(df_personal, on="customerID", how="left")
df = df.merge(df_phone, on="customerID", how="left")

# Imprimir el DataFrame fusionado
df

