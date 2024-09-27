#frutas = {"maçã", "abacaxi", "laranja"} #set (entre chaves) msm coisa q lista mas aleatorio

#frutas.add("mexirica") 
#frutas.remove("maçã")
#frutas.pop()

#print(frutas)

#set1 = {"maçã", "abacaxi", "laranja", "mexirica"}
#set2 = {0, 1, 2, 3, 4, 5}
#set3 = {True, False, True, False}
#set4 = {"arthur", 18, True}

#print(set1)
#print(set2)
#print(set3)
#print(set4)

meses = {
    "jan" : "janeiro",
    "fev" : "fevereiro",
    "mar" : "março",
    "abr" : "abril",
    "mai" : "maio",
    "jun" : "junho",
    "jul" : "julho",
    "ago" : "agosto",
    "set" : "setembro",
    "out" : "outubro",
    "nov" : "novembro",
    "dez" : "dezembro"
}

print(meses["mar"])
print(meses.get("abc", "nao existe"))
print(len(meses)) 