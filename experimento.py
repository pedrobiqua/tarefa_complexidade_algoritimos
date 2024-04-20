########## ALGORITIMOS EXTRAS ##########
from heap_sort import heapSort
from radix_sort import radixSort
########################################
from quick_sort_recursivo import quick_sort_recursivo_wapper
from quick_sort_random import quick_sort_recursivo_random_wapper
from merge_sort_interativo import Merge_Sort_interativo_wapper
from merge_sort_recursivo import merge_sort__recursivo_wapper
from merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from select_sort_recursivo import select_sort_recursivo_wapper
from select_sort_recursivo_random import select_sort_recursivo_random_wapper
from sellSort_base_line import shellSort_Wapper
from gerador import gerar_dados_crescente
from gerador import gerar_dados_random
from gerador import gerar_dados_decrescente
from gerador import agora
from gerador import dif_time
######### PANDAS #########
import pandas as pd

"""
X = [58, 30, 97, 21, 81, 35, 48, 59, 24, 2, -1]
print(f'X : {X}')

QS1 = quick_sort_recursivo_wapper(X.copy())
QS2 = quick_sort_recursivo_random_wapper(X.copy())
print(f'Quick sort recursivo: {QS1}')
print(f'Quick sort recursivo randomizado: {QS2}')

MS1 = Merge_Sort_interativo_wapper(X.copy())
MS2 = merge_sort__recursivo_wapper(X.copy())
MS3 = merge_sort_recursivo_random_wapper(X.copy())
print(f'Merge sort interativo: {MS1}')
print(f'Merge sort recursivo: {MS2}')
print(f'Merge sort recursivo randomizado: {MS3}')

SS1 = select_sort_recursivo_wapper(X.copy())
SS2 = select_sort_recursivo_random_wapper(X.copy())
print(f'Select sort recursivo: {SS1}')
print(f'Select sort recursivo randomizado: {SS2}')

BASE_LINE = shellSort_Wapper(X.copy())
print(f'Sell Sort [Baseline]: {BASE_LINE}')
"""

"""
Função de rotina de execuções
"""
def execucao(X):
    D = []

    a = agora()
    QS1 = quick_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    QS2 = quick_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    #a = agora()
    #MS1 = Merge_Sort_interativo_wapper(X.copy())
    #b = agora()
    #D.append(dif_time(b, a))

    a = agora()
    MS2 = merge_sort__recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    MS3 = merge_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    SS1 = select_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    SS2 = select_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    '''a = agora()
    BASE_LINE = shellSort_Wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    HPS = heapSort(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    RDX = radixSort(X.copy())
    b = agora()
    D.append(dif_time(b, a))'''

    return D

def testes(T=100, N=10, tipo="DSC"):
    L = []
    L_TAMANHOS = []
    if tipo == "DSC":
        # Dados decresente dos algoritimos
        for i in range(1, N, 1):
            tamanho = i * T
            X = gerar_dados_decrescente(tamanho)
            L.append(execucao(X))
            L_TAMANHOS.append(tamanho)
    elif tipo == "ASC":
        # Dados cresente dos algoritimos
        for i in range(1, N, 1):
            tamanho = i * T
            X = gerar_dados_crescente(tamanho)
            L.append(execucao(X))
            L_TAMANHOS.append(tamanho)
    elif tipo == "RNG":
        # Dados aleatórios dos algoritimos
        for i in range(1, N, 1):
            tamanho = i * T
            X = gerar_dados_random(tamanho)
            L.append(execucao(X))
            L_TAMANHOS.append(tamanho)
    else:
        return
    
    # Mostrar os resultados
    print('QS1,QS2,MS2,MS3,SS1,SS2')
    for x in L:
        c = len(x) - 1
        i = 0
        for y in x:
            if (i < c):
                print(y, end=',')
            else:
                print(y, end='')
            i +=1
        print()

    # Adicina a Coluna Final do tamanho do array
    Lista_final = []
    for i, lista in enumerate(L):
        Lista_final.append(lista + [L_TAMANHOS[i]])
    
    # Criar um DataFrame do Pandas
    df = pd.DataFrame(Lista_final, columns=['QS1', 'QS2', 'MS2', 'MS3', 'SS1', 'SS2', 'TAM'])

    # Salvar o DataFrame em um arquivo Excel
    df.to_excel(f'dados_{tipo}_{T}.xlsx', index=False)

# Bateria de testes
testes(T=100, N=10, tipo="DSC")
testes(T=100, N=10, tipo="ASC")
testes(T=100, N=10, tipo="RNG")