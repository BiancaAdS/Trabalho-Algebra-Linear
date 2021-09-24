#Alunos: André Luiz Coelho e Bianca Albuquerque da Silva
#Exercicio T1 - Teoria dos Grafos e Matrizes

import numpy as np

def criaMatrizVertice(n): #Cria a matriz de vertices, com n vertices tais que cada vertice esteja conectado a cada um outro vertice
    matriz = []
    for i in range(0, n):
        linha = []
        for j in range(0,n):
            if(i == j):
             linha.append(0)
            else:
                linha.append(1)
        matriz.append(linha)

    return matriz

def calcularConexoes(matrizA, k): #realiza o calculo do numero de passos da matriz de vertice ao calcular a potência k da matriz
    
    matriz = np.linalg.matrix_power(matrizA, k)
    
    return matriz 

def imprimir(matriz): #imprime a matriz formatada bonitinha
    for i in range(len(matriz)):
        print(matriz[i])


def main(args):

    n = int(input("Digite a ordem da matriz: "))
    k = int(input("Digite a quantidade de conexões: "))

    matriz = criaMatrizVertice(n)

    if(k == 1):
        imprimir(matriz)
        print()
        print("Não foram calculadas as conexões da matriz.") 
    else:
        imprimir(matriz)
        print()
        imprimir(calcularConexoes(matriz,k))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
