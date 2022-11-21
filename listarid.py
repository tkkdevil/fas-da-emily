def listar ():
    arquivo = open("cadrasto.csv", "r") 
    
    conteudo = arquivo.readlines()
    id = input("digite um id")

    a = len(conteudo)
    controle = False


    for n in range(2,a):
        linha = conteudo[n].split(";")

        if id == linha [0]:
            controle = True 
        
            print("id: " + linha [0])
            print("nome: " + linha [1])
            print("mtricula: " + linha [2])
            print("idade: " + linha [3])
            print("nota: " + linha [4])
            break
    
    arquivo.close()

    arquivo = open("cadrasto.csv", "w") 
    
    arquivo.writelines(conteudo)
    if controle == False:
        print ("nao existe")
listar()