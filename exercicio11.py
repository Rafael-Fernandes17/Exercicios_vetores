#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0
menor = 0
maior = 0

while indice < 5:
    
    #Inserindo os valores no vetor
    numeros = float(input("Digite um número qualquer: "))
    numerosLidos[indice] = numeros
    
    #Definindo o primeiro menor e o primeiro maior
    if indice == 0:
        menor = numerosLidos[0] 
        maior = numerosLidos[0]
        
    #Definindo o maior valor
    if numeros > maior:
        maior = numeros

        #Definindo a posição do maior valor
        posicaoMaior = indice
        
    #Definindo o menor valor
    if numeros < menor:
        menor = numerosLidos[indice]
        
        #Definindo a posição do menor valor
        posicaoMenor = indice
    indice += 1

#Exibindo o vetor, o maior número e sua posição, o menor número e a sua posição
print("\nOs valores que você inseriu foram: ", numerosLidos)
print("O maior número digitado foi: {} e ele se encontra no indice: {}".format(maior, posicaoMaior))
print("O menor número digitado foi: {} e ele se encontra no indice: {}".format(menor, posicaoMenor))
