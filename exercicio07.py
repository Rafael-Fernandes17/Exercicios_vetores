import random

#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Criando as outras variáveis
indice = 0
menor = 0
maior = 0

while indice < 10:
    
    #Inserindo valores no vetor
    numerosLidos[indice] = random.randint(-100, 100)
    
    #Defininfo o maior valor
    if numerosLidos[indice] > maior:
        maior = numerosLidos[indice]

        #Definindo o índice do maior valor
        posicaoMaior = indice
    
    
    indice += 1

#Exibindo o maior valor e o seu índice
print("\nOs valores do vetor são: ", numerosLidos)
print("O maior número encontrado no vetor foi: ", maior)