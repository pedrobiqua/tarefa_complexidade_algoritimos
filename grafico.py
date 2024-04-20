import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define a função linear que queremos ajustar aos dados.
def func(x, a, b):
    return a * x + b

# Carregar os dados do arquivo Excel
df = pd.read_excel('dados_ASC_10000.xlsx')
#df = pd.read_excel('dados_DSC_10000.xlsx')
#df = pd.read_excel('dados_RNG_10000.xlsx')

# Para cada algoritmo
for column in df.columns[:-1]:  # Ignorar a coluna 'TAM'
    # Coletar dados
    x = df['TAM']
    y = df[column]

    # Ajustar a função aos dados
    popt, pcov = curve_fit(func, x, y)

    # Prever o tempo de execução para um vetor duas vezes maior que o maior tamanho de entrada analisado
    prediction_x = 2 * max(x)
    prediction_y = func(prediction_x, *popt)

    # Adicionar a previsão ao conjunto de dados
    x = np.append(x, prediction_x)
    y = np.append(y, prediction_y)

    # Criar o gráfico
    plt.scatter(x[:-1], y[:-1], label=f'{column} Dados')  # Plot all points except the prediction
    plt.scatter(prediction_x, prediction_y, label=f'{column} Previsão')  # Plot the prediction point
    plt.plot(x, func(x, *popt), label=f'{column} Ajuste: y = {popt[0]:.4f}x + {popt[1]:.2f}')

# Configurar e exibir o gráfico
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução')
plt.title('Gráfico de Tendência para Algoritmos de Sort')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
