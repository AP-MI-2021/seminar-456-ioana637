from Domain.prajitura import create_prajitura

def add_prajitura(prajituri, id, nume, descriere, pret, calorii, an_introducere):
    '''
    Adaugam in memorie, in lista de prajituri o prajitura formata
    din fieldurile: id, nume, descriere, pret, calorii, an_introducere
    :param prajituri: lista de prajituri
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param calorii: int
    :param an_introducere: int
    :return:
    '''
    prajitura = create_prajitura(id, nume, descriere, pret, calorii, an_introducere)
    prajituri.append(prajitura)



