# Exercício Tecnológico T1 - Teoria dos Grafos e Matrizes
### **Alunos:** André Luiz Coelho Silva e Bianca Albuquerque da Silva

O código foi implementado para resolver um exercício de tecnologia sugerido no livro Álgebra Linear com Aplicações de Howard Anton e Chris Rorres, o exercício T1 letras (a), (b) e (f):

***Enunciado da Questão:***

<p align="center">
  <img src="https://github.com/BiancaAdS/Trabalho-Algebra-Linear/blob/main/ExercicioT1/images/T1.PNG" alt="enunciadoT1">
</p>

<p align="center">
  <img src="https://github.com/BiancaAdS/Trabalho-Algebra-Linear/blob/main/ExercicioT1/images/T1_ab.PNG" alt="nunciadoT1_a_b">
</p>

<p align="center">
  <img src="https://github.com/BiancaAdS/Trabalho-Algebra-Linear/blob/main/ExercicioT1/images/T1_f.PNG" alt="enunciadoT1_f">
</p>

***Funcionamento do código:***

Código foi dividido em 3 funções para a melhor compreensão e organização do mesmo. 
* A função **criaMatrizVertice(*n*)** é a função que gera a matriz nas diretrizes que foram especificadas no enunciado do exercício, recebendo apenas a ordem/tamanho da matriz para criar a mesma; 
* A função **calcularConexoes(*matrizA*, *k*)**, que é responsável por calcular o número de passos da matriz de vértice, nela foi utilizada a função de potência de matriz, do módulo *numpy*: **np.linalg.matrix_power(*matrizA*, *k*)**, onde recebe o número *k* de conexões e a *matriz de vértice* para calcular as conexões. A função **np.linalg.matrix_power()**, de acordo com a sua documentação, pega a matriz e um expoente como parâmetros de entrada e retorna o resultado da operação em outra matriz, assim, a matriz que foi resultada é a matriz que nos interessa, que contém as conexões da matriz de vértice; e
* A função **imprimir(*matriz*)**, que serve apenas para imprimir a matriz obtida de forma organizada, para melhor visualização dos elementos e ordem da matriz.


