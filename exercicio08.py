#Criando o vetor
numerosLidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Criando outras variáveis
indice = 1

while indice < 15:
    
    #Inserindo a nota dos alunos no vetor
    numerosLidos[indice] = float(input("Aluno {} - A nota foi: ".format(indice)))
    indice += 1
  
#Somando a nota dos alunos  
soma = (numerosLidos[0] + numerosLidos[1] + numerosLidos[2] + numerosLidos[3] + numerosLidos[4] + numerosLidos[5] + numerosLidos[6] + numerosLidos[7] + numerosLidos[8] + numerosLidos[9] + numerosLidos[10] + numerosLidos[11] + numerosLidos[12] + numerosLidos[13] + numerosLidos[14])

#Calculando a média das notas
media = soma/15

#Exibindo a média
print("A média geral da turma foi: ", media)