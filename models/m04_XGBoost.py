# Modelo  XGBoost

xgb_model = XGBClassifier(objective='binary:logistic')

# Define la cuadrícula de hiperparámetros a buscar
xgb_param_grid = {
    'max_depth': [3, 4, 5],          # Profundidad máxima del árbol
    'learning_rate': [0.1, 0.01],   # Tasa de aprendizaje
    'n_estimators': [40, 50, 60]     # Número de estimadores (número de árboles)
}

# Realiza una búsqueda de cuadrícula con validación cruzada
xgb_grid = GridSearchCV(estimator=xgb_model, param_grid=xgb_param_grid, scoring='roc_auc', cv=5, n_jobs=-1)
xgb_grid.fit(ohe_feat_train, ohe_tar_train)

# Obtiene los mejores parámetros y la mejor puntuación
xgb_best_params = xgb_grid.best_params_
xgb_best_score = xgb_grid.best_score_

print('Resultados de GridSearch para XGBoost')
print("\n La mejor puntuación:", xgb_best_score)
print("\n Los mejores parámetros:\n", xgb_best_params)