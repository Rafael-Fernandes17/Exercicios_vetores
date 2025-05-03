#Criando o vetor
numeros = [0, 0, 0, 0, 0, 0, 0]

#Atribuindo os valores no vetor
numeros[0] = 1
numeros[1] = 0
numeros[2] = 5
numeros[3] = -2
numeros[4] = -5
numeros[5] = 7
print("Primeira tabela: ", numeros)

#Armazenando a soma dos valores nas posicoes 0, 1 e 5
soma015 = numeros[0] + numeros[1] + numeros[5]
print("\nA soma das variáveis nas posições 0, 1 e 5 é: ", soma015,"\n")

#Alterando o valor na posição 4
numeros[4] = 100

#Exibindo os valores
print("Tabela modificada: ", numeros)
print("\nValor guardado na posição 0: ", numeros[0])
print("Valor guardado na posição 1: ", numeros[1])
print("Valor guardado na posição 2: ", numeros[2])
print("Valor guardado na posição 3: ", numeros[3])
print("Valor guardado na posição 4: ", numeros[4])
print("Valor guardado na posição 5: ", numeros[5])