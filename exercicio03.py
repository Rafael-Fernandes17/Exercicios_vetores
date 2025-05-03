#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Criando o vetor dos números na potência de 2
numerosQuadrados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 0

while indice <= 9:
    
    #Fazendo a lógica para inserir os valores em um vetor
    numeros = input("Digite um número qualquer: ")
    numeros = float(numeros)
    numerosLidos[indice] = numeros
    
    #Fazendo a lógica para calcular o quadrado desses valores
    numerosQuadrados[indice] = numeros**2
    indice += 1
    
#exibindo os vetores
print("\nOs valores que você inseriu foram: ", numerosLidos)
print("\nOs número inseridos elevados ao quadrado são: ", numerosQuadrados)



