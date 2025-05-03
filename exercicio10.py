#Craindo o vetor
numerosLidos = [0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0
menor = 0
maior = 0

while indice < 5:
    
    #Inserindo os valores no vetor
    numeros = int(input("Digite um valor inteiro: "))
    numerosLidos[indice] = numeros
    if indice == 0:
        menor = numerosLidos[0] 
        
    #Definindo o menor
    if numeros < menor:
        menor = numerosLidos[indice]
        
    #Definindo o maior
    if numeros > maior:
        maior = numeros
    indice += 1
    
#Somando os valores
soma = numerosLidos[0] + numerosLidos[1] + numerosLidos[2] + numerosLidos[3] + numerosLidos[4]

#Calculando a média dos valores
media = soma/4

#Exibindo o vetor, o maior valor, o menor valor, e a média dos valores
print("\nOs valores lidos foram: ", numerosLidos)
print("O maior valor lido foi: ", maior)
print("O menor valor lido foi: ", menor)
print("A média de todos os valores lido foi: ", media)
