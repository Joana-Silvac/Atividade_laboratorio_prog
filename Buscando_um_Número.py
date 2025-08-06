#Elabore uma função que receba um número e uma lista. A função deve buscar o número na lista e retornar 'True' se o encontrar e 'False' caso contrário.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
x=int(input("Digite um número e veja se esta na lista:"))
def buscar(x,numeros):
    encontrar= False
    if x in numeros:
        encontrar= True
    return print(encontrar)
buscar(x,numeros)