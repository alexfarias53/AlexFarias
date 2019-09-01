# listas

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista.append("limão")

                                    # pode ser qualquer coisa

# print(minha_lista[0])
# print(minha_lista[1])
# print(minha_lista[2])

                                     # usando o laço for
# for item in minha_lista:
# print(item)
# tamanho = len(minha_lista)
# print(tamanho)

                                    #add valores a lista
# print(minha_lista)

                                # saber se um elemanto existe na lista
# if "morango" in minha_lista:
    #print("morango pertence a lista")
#else:
    #print("não está na lista")

                                    #removendo item da lista
del minha_lista[2:] # para apagar a lista inteira [:]
print(minha_lista)
                                    #criar  uma lista em branco
minha_lista_4 = []
minha_lista_4.append(57)
print(minha_lista_4)
                                  #ordenar listas

lista = [124,345,5,72,46,6,7,3,1,7,0]
#lista.sort()  # esse metodo altera a lista existe e ordena
#print(lista)
lista = sorted(lista) # esse metodo retorna o valor e ordena ela
print(lista)

                               # ordenar em ordem reversa
lista.sort(reverse=True)

print(lista)

lista.reverse()
print(lista)






























