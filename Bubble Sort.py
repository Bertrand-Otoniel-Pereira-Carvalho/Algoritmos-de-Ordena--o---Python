import random

lista = []
for i in range(1,50):
    lista.append(random.randint(1,100))

soma = sum(range(0,(len(lista))-1))    #Realizando operações desnecessárias
aux = 0
for i in range(1,soma):
    for i in range(0,(len(lista))-1):
        if(lista[i] > lista[i+1]):
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux

print(lista)

condicional = True  # Realizando apenas a quantidade necéssaria de operações
while(condicional == True):
    condicional = False
    for i in range(0,(len(lista))-1):
        if(lista[i] > lista[i+1]):
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
            condicional = True
            
print(lista)
