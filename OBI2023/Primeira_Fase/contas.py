#Variáveis
V = int(input())
A = int(input())
F = int(input())
P = int(input())
contas_pagas = 0

#Verificando os limites de entrada
if V < 0 or V > 2000:
    print(0)
if A < 1 or A > 1000:
    print(0)
if F < 1 or F > 1000:
    print(0)
if P < 1 or P > 1000:
    print(0)

#Lista com contas
contas = [A,F,P]
contas = sorted(contas) #Ordenação da lista crescente

#Loop para percorrer a lista
for conta in contas:
    if V >= conta:  
        V -= conta  #Subtração para valor total
        contas_pagas += 1
    else:
        break
print(contas_pagas)     #Saída
