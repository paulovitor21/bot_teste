import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from flask import Flask, request, jsonify

# Busca dos Dados
dados_reviews = pd.read_csv('dados_reviews.csv')
print(dados_reviews.head())

# Treinamento dos Dados (Análise de Sentimentos usando NLP)
X = dados_reviews['review_text']
y = dados_reviews['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {acuracia}')

# Deploy da Solução com Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review_text = data['review_text']
    prediction = modelo.predict([review_text])[0]
    return jsonify({'sentiment': prediction})

if __name__ == '__main__':
    app.run(debug=True)
