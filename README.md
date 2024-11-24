# Risco de Crédito
![1_e6ap-Ofk3QhwZns73Bme_Q](https://github.com/igorrodlima/Portfolio-De-Projetos/assets/104405698/a4736e78-08ee-46da-8f74-b7efdf117165)

# Sobre o projeto


O projeto foi desenvolvido de forma independente com o objetivo de prever, por meio de um modelo de machine learning, se um cliente de uma instituição financeira será inadimplente. Em outras palavras, o propósito é antecipar a possibilidade de um cliente não cumprir com o pagamento de qualquer dívida, deixando de honrar o compromisso financeiro assumido.

Assim, o foco principal é auxiliar a empresa na tomada de decisão, tornando-a mais ágil e precisa, ao possibilitar a minimização de perdas e automatizar o processo de avaliação de crédito. Além disso, o projeto pode ajudar a direcionar recursos de marketing e vendas de forma mais eficaz, maximizando o retorno sobre o investimento em aquisição de clientes.
## Deploy do Modelo

![Deploy](https://github.com/igorrodlima/Portfolio-De-Projetos/assets/104405698/3b79901b-2591-48f0-95a2-3a34d051b64e)


## Métodos utilizados
- Análise Exploratória dos Dados
- Aprendizado de Máquina


# Tecnologias utilizadas
- Jupyter Notebook (Python)
- VSCode (Python, HTML)
  
# Descrição do Projeto
A base de dados foi obtida do Kaggle, uma plataforma de competição entre cientistas de dados, e consiste em 32.581 registros com 12 colunas. O objetivo primordial deste projeto é desenvolver um modelo de Machine Learning capaz de analisar um conjunto de variáveis e prever se um cliente é propenso ou não à inadimplência. Dessa forma, busca-se aprimorar a precisão das avaliações de risco, permitindo tomadas de decisões mais informadas e estratégicas no processo de concessão de crédito.

Durante a análise exploratória, o foco foi lidar com dados ausentes, nulos e possíveis outliers. Além disso, estudar as distribuições, extrair informações relevantes e identificar tendências por meio de visualizações gráficas.

No processo de construção do modelo, buscou-se maximizar o desempenho, realizando inicialmente a engenharia de atributos, adicionando 2 novas variáveis à base de treinamento. As variáveis categóricas e numéricas foram tratadas utilizando técnicas como One Hot Encoder e Standard Scaler.

Quatro algoritmos diferentes foram treinado (Random Forest, XGBoost, LightGBM e Redes Neurais) em três conjuntos de dados de treinamento distintos (apenas padronizado, com undersampling e com oversampling). Após o treinamento desses 12 modelos, aquele que apresentou o melhor desempenho foi selecionado para ser aplicado no deploy.

# Como utilizar
1. Instale as dependências necessárias.
2. Execute os notebooks como de costume, usando um servidor Jupyter Notebook, Vscode, etc.

# Contato
- igorrodlima03@gmail.com
- https://www.linkedin.com/in/igorrodlima/
