i = 1

#while i < 10:
#    print(i) 
#    i = i + 1
#print("i terminou")
#print(i)

lista1 = ["eu", "tu", "nois", "bota nela"]

#for x in lista1:
#    print(x)

canal = "refatorando"
#for letra in canal:
#    print(letra)
 
#for index in range(len(lista1)):
#    print(lista1[index], index)

#for index in range(5):
#    if index == 0:
#        print("primeira linha")
#    else:
#        print(f"outras linhas {index}")

#lista de listas (matriz)

matriz_numeros = [
[7, 8, 9],
[4, 5, 6],
[1, 2, 3],
[0],
]
for linha in matriz_numeros:
    #print(linha)
    print("---")
    for coluna in linha:
        print(coluna)