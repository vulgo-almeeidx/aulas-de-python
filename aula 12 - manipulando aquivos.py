#open("caminho", "r")

#r = leitura
#a = append
#w = write
#x = create
# r+ = leitura e escrita

#arquivo = open("test.txt", "r")

#print(arquivo.readable())
#print(arquivo.read())
#print(arquivo.readline())
#print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)
# print(lista[2])

#arquivo.close()


#arquivo = open("test3.txt", "x")
# arquivo.write("portugol\n")
# arquivo.write("inglesgol\n")
# arquivo.write("penisgol\n")

#arquivo.close()


import os

#if os.path.exists("test2.txt"):
#    os.remove("test2.txt")
#    print("aquivo deletado")
#else:
#    print("este arquivo nao existe ou ja foi deletado")

os.rmdir("aula12/aula 12 - manipulando aquivos.py")
print("pasta excluida com sucesso")
