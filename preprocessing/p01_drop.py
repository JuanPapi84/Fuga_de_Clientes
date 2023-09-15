# Eliminar las columnas que no son necesarias para el modelo
df= df.drop(columns=['customerID', 'BeginDate', 'EndDate', 'TotalService'])