# Modelo de Árbol de Decisión
dtc_param = {'max_depth': [20, 22, 24, 26, 28, 30]}

dtc_model = DecisionTreeClassifier(random_state=54321)
dtc_grid = GridSearchCV(estimator=dtc_model, param_grid=dtc_param, scoring='roc_auc', cv=5, n_jobs=-1, verbose=0)

dtc_grid.fit(ohe_feat_train, ohe_tar_train)

#Mejores parámetros
print('Resultados de GridSearch')
print("\n La mejor puntuación:", dtc_grid.best_score_)
print("\n Los mejores parámetros:\n", dtc_grid.best_params_)

dtc_best_param=dtc_grid.best_params_