def media ():
    arquivo = open("cadrasto.csv", "r") 
    
    conteudo = arquivo.readlines()
    a= len(conteudo)
    soma = 0

    for n in range (2 ,a):
        calcular = conteudo[n].split(";")
        receber = int(calcular[4])
        soma = receber + soma
    resultado = soma/(a-2)
    print(resultado)
