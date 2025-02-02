# -*- coding: utf-8 -*-
"""League_Project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JNMhuc1FbD1Xi1r-qFd8Xg9xHLGu-cnh

██╗░░░░░███████╗░█████╗░░██████╗░██╗░░░██╗███████╗  ██████╗░░█████╗░████████╗░█████╗░
██║░░░░░██╔════╝██╔══██╗██╔════╝░██║░░░██║██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██║░░░░░█████╗░░███████║██║░░██╗░██║░░░██║█████╗░░  ██║░░██║███████║░░░██║░░░███████║
██║░░░░░██╔══╝░░██╔══██║██║░░╚██╗██║░░░██║██╔══╝░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
███████╗███████╗██║░░██║╚██████╔╝╚██████╔╝███████╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║
╚══════╝╚══════╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚══════╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░

League of Legends competitive matches between 2015-2017. The matches include the NALCS, EULCS, LCK, LMS, and CBLoL leagues as well as the World Championship and Mid-Season Invitational tournaments.

dados - https://www.kaggle.com/code/jonathanbouchet/lol-games-4-years-of-esport/input

Script desenvolvido por Eduardo Silva Coqueiro (https://github.com/Edu-png)
"""

# 1. Impotando as bibliotecas as quais irei usar:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

# 2. Importando data set diretamente do Kaggle para o colab:

dt = pd.read_csv('/content/LeagueofLegends.csv')

# 3 Exploração inicial dos dados & Analises descritivas:

#3.1. Olhando os dados:
dt.head(10)

#3.3. Coletando informações sobre os dados:
dt.info()

#3.3. Observando valores estatísticos relevantes:
dt.describe()

#3.4. Vendo o número de linhas e colunas: (3760 linhas, 29 colunas)
dt.shape

#3.5. Verrificando se há valores nulos:
dt.isnull().sum()

# Não há nenhum valor nulo no nosso dt!

# 4. Pré-processamento dos dados:

# 4.1. Como vimos que não há valores nulos, não se faz necessário o processo de substituilos ou excluilos. Poderiamos:

# Remover linhas com valores ausentes
#dt_limpo = df.dropna()

# Ou preencher valores ausentes com a média
#dt['coluna'].fillna(dt['coluna'].mean(), inplace=True)

# 4.2. Ao observar os tipos de colunas, também vimos que não é necessário realizar nenhum tipo de mudança. Mas poderiamos usar:

#dt['coluna_name'] = pd.to_datetime(dt['data']) #por exemplo.

# 4.3. Outra coisa que poderiamos fazer é categorizar os dados numéricos em categóricas ou vice versa, mas no momento não iremos fazer isso.

# 5. Vamos fazer a visualização gráfica de algumas colunas importantes:

# 5.1. [Year]:

# Para ano primeiro temos que fazer o somatório dos valores por ano.
contagem_anos = dt['Year'].value_counts()

# Criar o histograma com a cor azul e barras largas
plt.bar(contagem_anos.index.astype(str), contagem_anos.values, color='skyblue', width=0.5) # Coloco o astype(str) para ter apenas os valores pontuais.

# Adicionar rótulos e título
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Total de partidas', fontsize=12)
plt.title('Distribuição de Partidas por Ano', fontsize=14)

# Ajustar o tamanho da figura
plt.figure(figsize=(8, 6))

# Mostrando o gráfico
plt.show()

# 5.2. [Season]:

season_count = dt['Season'].value_counts()
season_count

# Ajustar o tamanho da figura
plt.figure(figsize=(8, 6))

# Criar o histograma com a cor vermelha e barras largas
plt.bar(season_count.index.astype(str), season_count.values, color='red', width=0.5)

# Adicionar rótulos e título
plt.xlabel('Season', fontsize=12)
plt.ylabel('Total de partidas', fontsize=12)
plt.title('Distribuição de Partidas por Season', fontsize=14)

# Rotacionar os rótulos do eixo x em 45 graus
plt.xticks(rotation=45)

# Exibir o gráfico
plt.show()

# 5.3. [gamelength]:
plt3 = plt.hist(dt['gamelength'])
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma de uma Variável')
plt.show()