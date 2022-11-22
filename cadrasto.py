def cadrasto ():
    arquivo = open("cadrasto.csv", "r") 
    
    conteudo = arquivo.readlines()

    ultima_linha = conteudo[-1]
    resultado = ultima_linha.split(";")
    

    id= int (resultado[0])
    id = (id + 1)   

    arquivo.close()


    a = input("digite um nome")
    b = input("digite a matricula")
    c = input("digite a idade")
    d = input("digite a nota")

    arquivo = open("cadrasto.csv", "a")

    arquivo.write (str (id) + ";")
    arquivo.write(a + ";")
    arquivo.write(b + ";")
    arquivo.write(c + ";")
    arquivo.write(d + "\n")
    arquivo.close()
