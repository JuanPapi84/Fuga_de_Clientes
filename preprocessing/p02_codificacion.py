# Codificacion de las columnas categóricas para los modelos
ohe_df = pd.get_dummies(df, drop_first=True)

# Entrenamiento y prueba
ohe_train, ohe_test = train_test_split(ohe_df, test_size=0.25, random_state=12345)
print(ohe_train.shape)
print(ohe_test.shape)

# Escalamiento de los datos
numeric_val = ['MonthlyCharges', 'TotalCharges']
scaler = StandardScaler()
scaler.fit(ohe_train[numeric_val])
ohe_train[numeric_val] = scaler.transform(ohe_train[numeric_val])
ohe_test[numeric_val] = scaler.transform(ohe_test[numeric_val])

# Features y Target
ohe_features_train = ohe_train.drop(['ServiceContinue_Yes'], axis=1)
ohe_target_train = ohe_train['ServiceContinue_Yes']
ohe_features_test = ohe_test.drop(['ServiceContinue_Yes'], axis=1)
ohe_target_test = ohe_test['ServiceContinue_Yes']