# Modelo de Bosque Aleatorio
estimators = []
for i in range(1, 150, 10):
    estimators.append(i)

#diccionario de parámetros
rf_param = {
    'n_estimators' : estimators,
    'max_features' : [9, 11, 13, 15],
    'max_depth' : [10, 20, 30, 40]
}

rf = RandomForestClassifier(random_state=54321)
rf_grid = GridSearchCV(estimator=rf, param_grid=rf_param, scoring='roc_auc', cv=5, n_jobs=-1, verbose=0)

rf_grid.fit(ohe_feat_train, ohe_tar_train)

#Mejores parámetros
print('Resultados de GridSearch')
print("\n La mejor puntuación:", rf_grid.best_score_)
print("\n Los mejores parámetros:\n", rf_grid.best_params_)

rf_best_param=rf_grid.best_params_