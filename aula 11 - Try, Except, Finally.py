try:    
    numero = int(input("digite um numero: "))
    print(numero)
except ZeroDivisionError:
    print("divisao por zero nao é possivel")
except ValueError:
    print("digite um valor valido")
except:
    print("erro inesperado")
finally:
    print("sempre executa")