import random

#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0
pares = 0

while indice < 10:
    
    #Inserindo valores aleatórios no vetor
    numerosLidos[indice] = random.randint(1, 100)
    
    #Conferindo se são pares
    if numerosLidos[indice] % 2 == 0:
        pares += 1
    indice += 1

#Exibindo o vetor e quantos valores pares ele possui
print("\nO vetor possui os seguintes valores: ", numerosLidos)
print("\nO vetor possui {} valores pares".format(pares))



