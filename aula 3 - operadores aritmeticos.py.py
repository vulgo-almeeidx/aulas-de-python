"""conversao de tipos de variaveis"""
n1 = 5
print(n1)
print(type(n1))

a = float(n1)
print(type(a))

n2 = 7.9
print(n2)
print(type(n2))

b = int(n2)
print(type(b))

################################################################

""" operadores aritimeticos """

n3 = 10
n4 = 15

print(n3 + n4) #mais
print(n3 - n4) #menos
print(n3 * n4) #multiplicasao
print(n3 / n4) #divisao normal
print(n3 // n4) #divisao q resulta no numero inteiro
print(n3 % n4) #divisao q resulta no resto
print(n3 ** n4) #potenciasao

print((3 + 5) * (7 + 3))

print(abs(-10)) #abs mostra o numero absoluto(numero positivo independente de td)
print(abs(10))

print(pow(2,3)) #pow é abreviacao de power e faz potenciasao dos dois numero q botar
print(pow(9,4)) #n funciona se bota um numero so

print(max(1,6)) #mostra o numero maior
print(min(4,8)) #mostra o numero menor

print(round(8.9))
print(round(4.5)) #arredonda dependendo da proximidade com o proximo numero inteiro
print(round(2.6))

""" biblioteca de matematica """

import math #sempre usar math. pq é funcao importada

print(math.floor(5.6)) #floor arredonda pra baixo independente de proximidade
print(math.ceil(6.1)) #ceil arredonda pra cima independente de proximidade
print(math.sqrt(2)) #sqrt é raiz quadra ovibiamente (sempre devolve float) 
print(math.sqrt(49))