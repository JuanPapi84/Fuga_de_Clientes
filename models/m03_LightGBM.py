# Modelo de LightGBM

model=LGBMClassifier(objective='binary')

lgbm_param = {
    'num_leaves': [20, 30, 40],
    'learning_rate': [0.5, 0.1, 0.01],
    'n_estimators': [40, 50, 60]
}

lgbm_grid = GridSearchCV(estimator=model, param_grid=lgbm_param, scoring='roc_auc', cv=5, n_jobs=-1)
lgbm_grid.fit(ohe_feat_train, ohe_tar_train)
lgbm_best_param=lgbm_grid.best_params_

print('Resultados de GridSearch')
print("\n La mejor puntuación:", lgbm_grid.best_score_)
print("\n Los mejores parámetros:\n", lgbm_grid.best_params_)