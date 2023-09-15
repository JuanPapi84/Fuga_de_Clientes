# Para el modelo de cordura voy a usar una Regresión Logistica
lr_model = LogisticRegression(solver='liblinear')
lr_model.fit(ohe_feat_train, ohe_tar_train)
lr_predict = lr_model.predict(ohe_feat_train)
lr_acc=accuracy_score(ohe_tar_train, lr_predict)
lr_probab=lr_model.predict_proba(ohe_feat_train)
lr_auc=roc_auc_score(ohe_tar_train, lr_probab[:,1])
print('AUC-ROC =', lr_auc)
print('Accuracy =', lr_acc)