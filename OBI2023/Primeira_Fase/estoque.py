#Primeira linha de entrada
tiposN, tiposM = map(int, input().split()) #o map aplica a função int para cada elemento iterável

#Matriz
matriz = []

#Variáveis
Vendidas = 0

#Preenchendo a matriz linha por linha
for _ in range(tiposM): #Usamos range pois tiposM é um inteiro, não um interável
    linha = list(map(int, input().split())) #Lista de inteiros para a linha atual
    matriz.append(linha) #Adiciona a linha na matriz

#Pedidos
pedidos = int(input())

#Vendo as solicitações
for _ in range(pedidos):
    I, J = map(int, input().split()) #Tamanho e tipo solicitados

    #Ajuste de índices
    I -= 1
    J -= 1

    if matriz[I][J] > 0:    #Aqui vamos direto para a roupa e tamanho, para ver se ela tem estoque
        matriz[I][J] -= 1   #Reduz o estoque
        Vendidas += 1       #Incrementa o número vendido 

#Saída
print(Vendidas)