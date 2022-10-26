def nomes ():
    menu = []

    while(True):
        print("1 cadastro do aluno")
        print("2 listar todos os alunos")
        print("3 listar alunos em especifico")
        print("4 atualizar aluno")
        print("5 excluir aluno")
        print("ätualizar aluno")
        print("7 media")
        print("0 sair")
        
        numero_da_opcao = int(input("digite o numero da opcao"))

        if(numero_da_opcao <= 7 and numero_da_opcao >= 0):
            return numero_da_opcao                 

        menu.append(numero_da_opcao)
print()
print(nomes())