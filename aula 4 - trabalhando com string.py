minha_string = "     Qualquer Texto Ai De Teste. "

varias_linhas = """linha1, 
linha2,
linha3.""" #\n tbm serve pra quebrar linha na msm linha do codigo

nome = "arthur da rocha almeida"

x = "Texto" in minha_string #verifica se existe determinada palavra ou letra na string
print(x)

escrever_aspas = "pra escrever aspas faz \" q aparece \""


print(minha_string)

print(minha_string.upper())  # deixa tds as letras maiusculas
print(minha_string.lower())  # deixa tds minusculas
print(minha_string.capitalize())  # deixa só a primeira do paragrafo maiuscula

print(minha_string.isupper())  # verifica se o texto ta td em maiusculo
print(minha_string.islower())  # verifica se ta minusculo

print(minha_string.strip())  # tira espaços antes e dps do texto

print(minha_string.replace("e", "3")) #troca uma palavra ou letra do seu texto por outra

print(len(minha_string)) #len mostra qnts caracteres tem na string
print(len(nome))

print(nome[0]) #pega só determinada letra da string
print(nome[-2]) #msm coisa só q de tras pra frente
print(minha_string.index("t")) #vc mostra a letra e ele fala a posiçao da letra 
print(minha_string.index("Teste")) #tbm faz com palavra inteira

print(varias_linhas)