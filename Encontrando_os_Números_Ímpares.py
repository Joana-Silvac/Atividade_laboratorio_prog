

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def impar(numeros):
    x=list(filter(lambda x: x%2!=0, numeros))
    for i in x:
        print(i)
    return
impar(numeros)