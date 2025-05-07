#Pratica 1
# numeros = [5, 7, 12, 2, 9, 21]

# print(numeros)
# print(numeros[0])
# print(numeros[1])
# print(numeros[2])
# print(numeros[3])
# print(numeros[4])
# print(numeros[5])

#Pratica 2
# numeros = [5, 7, 12, 2, 9, 21]

# numeros[1] = 17
# numeros[3] = 22
# print(numeros)

# numeros[2] = 1
# numeros[4] = 29
# print(numeros)

#Pratica 3
# numeros = [5, 7, 12, 2, 9, 21]

# numeros[1] = 17
# numeros[3] = 22
# print(numeros)

# numeros[2] = 1
# numeros[4] = 29
# print(numeros)

# soma = numeros[5] + numeros[4]
# print(soma)

# subtracao = numeros[3] - numeros[1]
# print(subtracao)

# multiplicacao = numeros[0] * numeros[5]
# print(multiplicacao)

# divisao = numeros[3]/numeros[2]
# print(divisao)

#Pratica 4
# numeros = [5, 17, 1, 22, 29, 21]
# indice = 0

# while indice < 6:
#     print(numeros[indice] * 2)
#     indice += 1

#Desafio da aula: Implemente um programa em Python para verificar quantos númerosuma aposta acertou na Mega Sena. O programa deve ler do teclado
#os 6 números apostados e comparar com os 6 números sorteados. Ao final, o programa deve exibir os números sorteados, números jogados e quantidade de acertos.
#Obs: Faça essa atividade usando apenas os conceitos de vetores, sem utilizar nenhuma funcionalidade de listas.

# import random

# indice = 0
# quantosAcertou = 0
# numerosSorteados = [0, 0, 0, 0, 0, 0]
# numerosJogados = [0, 0, 0, 0, 0, 0]



# while indice < 6:
#     numerosSorteados[indice] = random.randint(1, 15)
    
#     while True:
#         respostaJogador = input("Aposte um número de 1 a 15: ")
#         if respostaJogador.isdigit(): # ele verifica se o usuário digitou apenas números.
#             respostaJogador = int(respostaJogador) # se for numero ele converte para int.
#             if respostaJogador > 0 and respostaJogador <= 15:  
#                 break
#             else:
#                 print("Resposta inválida! Digite novamente\n")
#             continue
#         else:
#             print("Resposta inválida! Digite novamente\n")
#             continue    
#     numerosJogados[indice] = respostaJogador
#     if numerosJogados[indice] == numerosSorteados[indice]:
#         quantosAcertou += 1
#     indice += 1
# print("Os números da sorte eram: ", numerosSorteados)
# print("Os numeros que você jogou foram: ", numerosJogados)
# print("Você acertou: ", quantosAcertou, " números")

