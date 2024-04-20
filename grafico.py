import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define a função linear que queremos ajustar aos dados.
def func(x, a, b):
    return a * x + b

# Carrega os dados do arquivo Excel
df = pd.read_excel('dados_ASC_100000.xlsx')
#df = pd.read_excel('dados_DSC_100000.xlsx')
#df = pd.read_excel('dados_RNG_100000.xlsx')
#f = pd.read_excel('dados_ASC_100.xlsx')
#df = pd.read_excel('dados_DSC_100.xlsx')
#df = pd.read_excel('dados_RNG_100.xlsx')


# Definir o tamanho do gráfico
plt.figure(figsize=(12, 8))

# Para cada algoritmo
markers = ['o', 'v', '^', '<', '>', 's', 'p', '*']  # Diferentes marcadores para cada algoritmo
for i, column in enumerate(df.columns[:-1]):  # Ignorar a coluna 'TAM'
    # Coletar dados
    x = df['TAM']
    y = df[column]

    # Ajustar a função aos dados
    popt, pcov = curve_fit(func, x, y)

    # Prevê o tempo de execução para um vetor duas vezes maior que o maior tamanho de entrada analisado
    prediction_x = 2 * max(x)
    prediction_y = func(prediction_x, *popt)

    # Adiciona a previsão ao conjunto de dados
    x = np.append(x, prediction_x)
    y = np.append(y, prediction_y)

    # Criar o gráfico
    plt.scatter(x[:-1], y[:-1], label=f'{column} Dados', marker=markers[i % len(markers)])  # Plot da previsão
    plt.scatter(prediction_x, prediction_y, label=f'{column} Previsão', marker=markers[i % len(markers)])  # Plot do ponto previsto
    plt.plot(x, func(x, *popt), label=f'{column} Ajuste: y = {popt[0]:.4f}x + {popt[1]:.2f}')

# Configuração e exibição do gráfico
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução')
plt.title('Gráfico de Tendência para Algoritmos de Sort em ordem Randômica')
plt.grid(True)
plt.legend(loc='best', fontsize='small')
plt.show()
