import random

#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0

while indice < 8:
    
    #Fazendo a lógica para inserir os valores em um vetor
    numeros = int(input("Digite um valor inteiro: "))
    numerosLidos[indice] = numeros
    
    #Fazendo a lógica para selecionar 2 números aleatŕios no vetor
    if indice >= 7:
        numeroSorteado1 = random.randint(0, 7)
        numeroSorteado2 = random.randint(0, 7)
    
    #Aumentando o índice
    indice += 1
    
#Calculando a soma dos números sorteados
somaNumeros = numerosLidos[numeroSorteado1] + numerosLidos[numeroSorteado2] 
print("\nOs valores que você inseriu foram: ", numerosLidos)
print("Os dois números aleatórios que foram selecionados para realizar a soma foram: ", numerosLidos[numeroSorteado1], "e" ,numerosLidos[numeroSorteado2])
print("A soma desses valores é: ", somaNumeros)


