import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# Carregar os dados
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(url, sep=';')

# Processar os dados
X = data.drop('quality', axis=1)  # Features
y = data['quality']  # Target

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo
model = Sequential()
model.add(Dense(1, input_dim=X.shape[1]))

# Compilar o modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Treinar o modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=0)

# Analisar o modelo
mse = model.evaluate(X_test, y_test)
print(f'MSE (Erro Quadrático Médio) no conjunto de teste: {mse}')

# Fazer predições
y_pred = model.predict(X_test)

# Analisar os resultados
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True vs. Predicted Values')
plt.show()

print(f'R² Score: {r2_score(y_test, y_pred)}')
