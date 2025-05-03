import random

#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0
menor = 0
maior = 0


while indice < 10:
    
    #Inserindo valores no vetor
    numeros = int(input("Digite um valor inteiro: "))
    numerosLidos[indice] = numeros

    if indice == 0:
        menor = numerosLidos[0] 
        
    #Conferindo o menor valor
    if numeros < menor:
        menor = numerosLidos[indice]
        
    #Conferindo o maior valor
    if numeros > maior:
        maior = numeros
    indice += 1
print("\nOs valores que você inseriu foram: ", numerosLidos)
print("O maior número digitado foi: ", maior)
print("O menor número digitado foi: ", menor)