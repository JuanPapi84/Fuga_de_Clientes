# Modelo Catboost

cb_model = CatBoostClassifier()

#diccionario de parámetros
cb_param = {
    'depth' : [6, 8, 10],
    'learning_rate' : [0.05, 0.1],
    'iterations' : [50, 100, 120]
}

cb_grid = GridSearchCV(estimator=cb_model, param_grid=cb_param, scoring='roc_auc', cv=5, n_jobs=-1, verbose=0)

cb_grid.fit(ohe_feat_train, ohe_tar_train)

print('Resultados de GridSearch')
print("\n La mejor puntuación:", cb_grid.best_score_)
print("\n Los mejores parámetros:\n", cb_grid.best_params_)

cb_best_param=cb_grid.best_params_