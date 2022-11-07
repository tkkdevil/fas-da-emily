def listar ():
    arquivo = open("cadrasto.csv", "r") 
    
    conteudo = arquivo.readlines()
    a = len(conteudo)
    for n in range(2,a):
        ultima_linha = conteudo[n].split(";")
        print("id: " + ultima_linha [0])
        print("nome: " + ultima_linha [1])
        print("mtricula: " + ultima_linha [2])
        print("idade: " + ultima_linha [3])
        print("nota: " + ultima_linha [4])
listar()


