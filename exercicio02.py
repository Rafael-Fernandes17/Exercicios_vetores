#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0

while indice < 6:
    
    #Lendo os valores
    numeros = int(input("Digite um valor inteiro: "))
    numerosLidos[indice] = numeros
    indice += 1

#Exibindo os valores
print("\nOs valores que você inseriu foram: ", numerosLidos)




