import getpass
passoword = 1234
correto = "sim"
print("+++++++++++++Seja Bem vindo+++++++++++++")
while correto == "sim":
    nome = input("Digite seu nome")
    print("Seja bem vindo", nome)
    senha = int(getpass.getpass("Agora digite a senha\n"))
    if senha == passoword:
     print("usuario aceito")
     n1 = int(input("primeiro numero"))
     n2 = int(input("segundo numero"))
     opcao = 0
     while opcao != 5:
      print('''      [1] somar
      [2] multiplicar
      [3] maior
      [4] novos numeros
      [5] sair do programa''')
      opcao = int(input(">>>>>>>>Qual é a sua opção?"))
      if opcao == 1:
       soma = n1 + n2
       print(" A soma ente {} + {} é {}".format(n1, n2, soma))
      elif opcao == 2:
       produto = n1*n2
       print(" O produto ente {} + {} é {}".format(n1, n2, produto))
      elif opcao == 3:
         if n1 > n2:
          maior = n1
         else:
          maior = n2
         print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))

      elif opcao == 4:
         print("informe os números novamente:")
         n1 = int(input("Primeiro valor"))
         n2 = int(input("Segundo valor:"))
      elif opcao == 5:
         print("Finalizando")
      else:
          print("opção invalida. Tente novamente")
      print("=-=" * 10)
      print("Fim do programa! Volte Sempre!")
print("usuario invalido")
quit()




