lista=[]

while True:
    x=input("Digite algo: ").lower().strip()
    if not x:
        break
        
    lista.append(x)
        

def vazia(lista):
    vazio=False
    if not lista:
        vazio=True

    return vazio

print(vazia(lista))