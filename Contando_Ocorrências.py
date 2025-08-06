numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

x=int(input("Digite o número e veja quantas vejes aparece na lista"))

def quantas(n,numeros):
    print(f"{numeros.count(n)} vez(es)")
    return
quantas(x,numeros)