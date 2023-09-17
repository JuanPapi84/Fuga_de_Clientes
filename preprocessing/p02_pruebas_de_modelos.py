# Voy a probar los 2 modelos con mejores resultados

# Crear un modelo LightGBM con los mejores parámetros
best_lgbm_model = LGBMClassifier(
    num_leaves=lgbm_grid.best_params_['num_leaves'],
    learning_rate=lgbm_grid.best_params_['learning_rate'],
    n_estimators=lgbm_grid.best_params_['n_estimators'],
    objective='binary',
    random_state=42
)

# Entrenar el modelo con los datos de entrenamiento
best_lgbm_model.fit(ohe_features_train, ohe_target_train)

# Realizar predicciones en el conjunto de prueba (ohe_feat_test)
lgbm_predictions = best_lgbm_model.predict(ohe_features_test)

# Calcular el AUC-ROC
lgbm_probabilities = best_lgbm_model.predict_proba(ohe_features_test)[:, 1]
lgbm_auc_roc = roc_auc_score(ohe_target_test, lgbm_probabilities)

# Calcular la precisión (Accuracy)
lgbm_accuracy = accuracy_score(ohe_target_test, lgbm_predictions)

# Imprimir los resultados
print('Resultados del modelo LightGBM con mejores parámetros:')
print('AUC-ROC =', lgbm_auc_roc)
print('Accuracy =', lgbm_accuracy)



# Crear un modelo CatBoost con los mejores parámetros
best_cb_model = CatBoostClassifier(
    depth=cb_grid.best_params_['depth'],
    learning_rate=cb_grid.best_params_['learning_rate'],
    iterations=cb_grid.best_params_['iterations'],
    verbose=0  # Puedes ajustar el nivel de verbosidad según tu preferencia
)

# Entrenar el modelo con los datos de entrenamiento
best_cb_model.fit(ohe_feat_train, ohe_tar_train)

# Realizar predicciones en el conjunto de prueba (ohe_feat_test)
cb_predictions = best_cb_model.predict(ohe_features_test)

# Calcular el AUC-ROC
cb_probabilities = best_cb_model.predict_proba(ohe_features_test)[:, 1]
cb_auc_roc = roc_auc_score(ohe_target_test, cb_probabilities)

# Calcular la precisión (Accuracy)
cb_accuracy = accuracy_score(ohe_target_test, cb_predictions)

# Imprimir los resultados
print('Resultados del modelo CatBoost con mejores parámetros:')
print('AUC-ROC =', cb_auc_roc)
print('Accuracy =', cb_accuracy)