def atualizar():
    arquivo = open("cadrasto.csv", "r") 
    conteudo = arquivo.readlines()

    id = input("digite um id")

    a = len(conteudo)
    controle = False
    
    for n in range(2,a):
        linha = conteudo[n].split(";")

        if id == linha[0]:
            controle = True

            linha[1] = input("digite um nome")
            linha[2] = input("digite a matricula")
            linha[3] = input("digite a idade")
            linha[4] = input("digite a nota")
            
            conteudo[n] = linha[0] + ";" + linha[1] + ";" + linha[2] +";" +  linha[3] + ";" + linha[4] + "\n"
            break
    arquivo.close()

    arquivo = open("cadrasto.csv", "w")
    arquivo.writelines(conteudo)
    if controle == False:
        print("nao existe")
atualizar()
