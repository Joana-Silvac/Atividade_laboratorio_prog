#Crie uma função que receba uma lista de objetos (onde cada objeto tem um atributo 'nome') e retorne uma nova lista contendo apenas os nomes de cada objeto.
class principal:
    def __init__(self,nome):
        self.nome=nome

todos_objetos=[]
while True:
    x=input("Digite o nome(ou sair):").lower().strip()
    
    if x!="sair":
        objeto=principal(x)
        todos_objetos.append(objeto)
    else:
        break
        
        
def mostrar(todos_objetos):
    return [obj.nome for obj in todos_objetos]
          
lista=mostrar(todos_objetos)
print(lista)