import menu 
import media
import listar
import excluir
import cadrasto
import atualizar
import listarid

def final():
    while(True):
        a = menu.nomes()
        if a == 1:
            cadrasto.cadrasto()
        
        elif a == 2:
            listar.listar()

        elif a == 3:
            listarid.listar()

        elif a == 4:
            atualizar.atualizar()

        elif a == 5:
            excluir.excluir()

        elif a == 6:
            media.media()

        elif a == 0:
            break
            

final()


# media.media()
# listar.listar()
# excluir.excluir()
# cadrasto.cadrasto()
# atualizar.atualizar()
# listarid.listar()