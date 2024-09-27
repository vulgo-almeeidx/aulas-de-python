#def big_mc():
#    print("saunduiche big mc")

#print("inicio")
#big_mc()
#print("fim")

def fazer_big_mc(nome):
    print(f"sanduiche big mc {nome}")

#fazer_big_mc("arthur")
#fazer_big_mc("lucilene")
#fazer_big_mc("chloe")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo, tamanho):
    print(f"{tipo} {tamanho}")

#fazer_big_mc("arthur")
#fazer_batata("media")
#preparar_refrigerante("coca", "grande")

def fazer_combo(nome, tamanho_batata, tipo_refrigerante, tamanho_refrigerante):
    fazer_big_mc(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refrigerante, tamanho_refrigerante)

#fazer_combo("arthur", "grande", "guarana", "media")

def soma_num(num1, num2):
    return num1 + num2 

#resultado = soma_num(15, 45)
#print(resultado)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([121, 13123, 849181, 82, 2])
print(resultado)