A, B = map(int, input().split())  #Inserindo o tamanho da sequência A e da sequência B

sequencia_a = []    #Lista A
sequencia_b = []    #Lista B

sequencia_a = list(map(int, input().split()))   #Input com separador
sequencia_b = list(map(int, input().split()))

#Controles de index
index_a = 0
index_b = 0

#Loop para percorrer e comparar
while index_a < A and index_b < B:
    if sequencia_a[index_a] == sequencia_b[index_b]:
        index_b += 1  # Avança em B apenas se houver correspondência
    index_a += 1  # Sempre avança em A

# Se conseguimos percorrer toda a sequência B, então ela é uma subsequência de A
if index_b == B:
    print("S")
else:
    print("N")