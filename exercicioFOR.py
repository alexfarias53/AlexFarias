
numero = input("digite um numero para tabuada:\n")
nomedoarquivo = ("Tabuada do " + numero)
for x in range(11):
    arquivo = open(str(nomedoarquivo), 'a')
    resultado =str(numero) + "*" + str(x) + "=" + str(int(numero) * x)
    print(resultado)
    arquivo.write(resultado + "\n")
    arquivo.close()
W = open("tabuada.txt", "w")
print("arquivo da", nomedoarquivo, "criado com sucesso")





