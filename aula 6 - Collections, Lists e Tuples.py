familia = ["arthur", "lucilene", "chloe", "luna", "júlia"]
familia2 = ["vó","vô", "tatinha"]
#print(familia[0]) #escolhe qual elemento da lista vc quer
#print(familia[-2]) # escolhe de tras pra frente
#print(familia[1:4]) # escolhe de tal elemento a tal elemento (exclui o ultimo)
#print(familia[2:]) # escolhe de tal elemento em diante

familia[3] = "lunatica" # muda o nome de qq elemento da lista
#print(familia)

familia.extend(familia2) #coloca outra lista dentro da primeira
#print(familia)

familia.append("tio fabinho") #coloca outros elementos individuais dentro da lista
#print(familia)

familia.insert(3, "belinha") #coloca outro elemento na lista mas agr tem q escolher a posiçao
#print(familia)

#familia.pop(5) #remove só 1 elemento (o ultimo se deixar em branco)
#familia.remove("lunatica") # faz a msm merda n sei nem pra q existe
#print(familia)

#familia.clear() # tem q deixar em branco pra remover a lista inteira
#print(familia)

#print(familia.index("tatinha")) # mostra o indice do elemento q vc quer com base no nome

#familia.append("arthur")
#print(familia.count("arthur")) # conta qnts elementos iguais tem na lista

idade_familia = [18, 43, 7, 6, 1, 18, 71, 84, 41, 50]
#idade_familia.sort() # organiza do menor pro maior se for numero
#print(idade_familia)

#familia.sort() # organiza em ordem alfabetica se for string
#print(familia)
#idade_familia.sort() # esse organiza a lista em ordem crescente ou alfabetica
#idade_familia.reverse() # esse inverte pra lista ficar em ordem decrescente

#familia3 = familia # "copia" uma lista mas só referenciando a lista original
#print(familia3)
#familia.pop(0)
#print(familia3) 

#familia3 = familia.copy() # cria uma copia independente da lista original
#print(familia3)
#familia.pop(0)
#print(familia3) 

#coordenadas = (378, 86, 294) # tuple fica entre parenteses e n pode ser alterado posteriormente
#coordenadas.pop()
#print(coordenadas)