#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0
negativos = 0
soma = 0

while indice <= 9:
    
    #Inserindo os valores no vetor
    numeros = input("Digite um número qualquer: ")
    numeros = float(numeros)
    numerosLidos[indice] = numeros
    
    #Verificando se o número é negativo
    if numerosLidos[indice] < 0:
        negativos += 1
        
    #Verificando e somando os números que são positivos
    elif numerosLidos[indice] >= 0:
        soma = soma + numerosLidos[indice]
    indice += 1
    
#Exibindo o vetor, a quantidade de valores negativos e a soma dos valores positivos
print("\nOs valores que você inseriu foram: ", numerosLidos)
print("Nesse vetor possui {} valores negativos.".format(negativos))
print("A soma dos valores positivos desse vetor é: ", soma)



