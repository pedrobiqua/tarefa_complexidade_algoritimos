import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Define a função linear que queremos ajustar aos dados.
def func(x, a, b):
    return a * x + b


# Carrega os dados do arquivo Excel
df = pd.read_excel('dados_ASC_100.xlsx')
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
    plt.scatter(x[:-1], y[:-1], label=f'{column} Dados', marker=markers[i % len(markers)])
    plt.scatter(prediction_x, prediction_y, label=f'{column} Previsão', marker=markers[i % len(markers)])
    plt.plot(x, func(x, *popt), label=f'{column} Ajuste: y = {popt[0]:.4f}x + {popt[1]:.2f}')

    # Print da predição do tempo para um tamanho de 3x, 4x e 5x do dados
    for j in range(3, 6):
        prediction_x_j = j * max(x)
        prediction_y_j = func(prediction_x_j, *popt)
        print(f'Predição do tempo em Milissegundos para um tamanho {j}x dos dados {column}: {prediction_y_j}')


# Configuração e exibição do gráfico
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução')
plt.title('Gráfico de Tendência para Algoritmos de Sort em ordem Ascendente')
plt.grid(True)
plt.legend(loc='best', fontsize='small')
plt.show()
