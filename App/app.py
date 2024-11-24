# Importando as bibliotecas
from flask import Flask, render_template, request
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='infrequent_if_exist')

import joblib
import pandas as pd

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Carregando o modelo de previsão de inadimplência
modelo = joblib.load(r'C:\Users\Eduardo\Documents\Risco Crédito\modelo.pkl')

# Função para calcular a categoria de renda com base no valor de renda
def calculando_categorias_renda(renda):
    categorias_renda = ['Até 10K', '10k - 20k', '20k - 40k', '40k - 80k', '80k - 160k', '160k +']
    limiar_values = [0, 10000, 20000, 40000, 80000, 160000]
    for i in range(len(limiar_values) - 1):
        if renda <= limiar_values[i + 1]:
            return categorias_renda[i]
    return categorias_renda[-1]

# Função para calcular a categoria de idade com base na idade
def calculando_categorias_idade(idade):
    categorias_idade = ['Até 25', '25 - 35', '35 - 45', '45 - 55', '55 - 65', '65+']
    for i, limiar in enumerate([0, 25, 35, 45, 55, 65]):
        if idade <= limiar:
            return categorias_idade[i]
    return categorias_idade[-1]

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')  # Renderiza o modelo HTML 'index.html'

# Rota para prever a inadimplência
@app.route('/predict', methods=['POST'])
def prevendo_inadimplencia():
    try:
        # Obtendo valores das features da requisição
        features = {
            'person_age': float(request.form['person_age']),
            'person_income': float(request.form['person_income']),
            'person_home_ownership': request.form['person_home_ownership'],
            'person_emp_length': float(request.form['person_emp_length']),
            'loan_intent': request.form['loan_intent'],
            'loan_grade': request.form['loan_grade'],
            'loan_amnt': float(request.form['loan_amnt']),
            'loan_int_rate': float(request.form['loan_int_rate']),
            'loan_percent_income': float(request.form['loan_percent_income']),
            'cb_person_default_on_file': request.form['cb_person_default_on_file'],
            'cb_person_cred_hist_length': float(request.form['cb_person_cred_hist_length']),
        }

        # Calculando as categorias 'Categorias_Renda' e 'Categorias_Idade'
        features['Categorias_Renda'] = calculando_categorias_renda(features['person_income'])
        features['Categorias_Idade'] = calculando_categorias_idade(features['person_age'])

        # Criando um DataFrame com as features
        df = pd.DataFrame([features])

        # Fazendo a predição usando o modelo
        predicao = modelo.predict(df)[0]
        predicao_proba = modelo.predict_proba(df)

        # Formatando o resultado da previsão
        resultado = f"Com {predicao_proba[0][1]*100:.2f}% de confiança, o cliente será inadimplente." if predicao == 1 else f"Com {predicao_proba[0][0]*100:.2f}% de confiança, o cliente não será inadimplente."

        return render_template('index.html', resultado=resultado, predicao_proba=predicao_proba)

    except Exception as e:
        return render_template('index.html', resultado=f"Erro na previsão: {str(e)}")

# # Executando o aplicativo Flask
# if __name__ == '__main__':
#     app.run(debug=True)  # Iniciando o servidor Flask em modo de depuração se este script for executado diretamente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
