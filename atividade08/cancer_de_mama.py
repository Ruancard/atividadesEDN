from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split

#Carregar os dados
data= load_breast_cancer()

x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

#Criar e treinar modelo
model = RandomForestClassifier()
model.fit(x_train, y_train)

#Reaclizar previsões

y_pred = model.predict(x_test)
y_pred_proba = model.predict_proba(x_test)[:,1]

#Avaliar modelo
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1score = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

#Exibir os dados
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 score: {f1score:.2f}")
print(f"ROC AUC: {roc_auc:.2f}")