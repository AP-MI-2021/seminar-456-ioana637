def create_prajitura(id, nume, descriere, pret, nr_calorii, an_introducere_meniu):
    '''

    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param nr_calorii: int
    :param an_introducere_meniu: int
    :return: Dict
    '''
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "nr_calorii": nr_calorii,
        "an_introducere_meniu": an_introducere_meniu
    }

def get_id(prajitura):
    '''

    :param prajitura: Dict
    :return: id - string
    '''
    return prajitura['id']

def get_nume(prajitura):
    '''

    :param prajitura: Dict
    :return: nume - string
    '''
    return prajitura['nume']

def get_descriere(prajitura):
    '''

    :param prajitura: Dict
    :return: descriere - string
    '''
    return prajitura['descriere']

def get_pret(prajitura):
    '''

    :param prajitura: Dict
    :return: pret - float
    '''
    return prajitura['pret']

def get_nr_calorii(prajitura):
    '''

    :param prajitura: Dict
    :return: nr_calorii - int
    '''
    return prajitura['nr_calorii']

def set_nr_calorii(prajitura, nr_calorii):
    '''
    Setarea nr_Calorii la prajitura
    :param prajitura: Dict
    :param nr_calorii: int
    :return:
    '''
    prajitura['nr_calorii'] = nr_calorii

def get_an_introducere(prajitura):
    '''

    :param prajitura: Dict
    :return: an_introducere - int
    '''
    return prajitura['an_introducere_meniu']

def to_str(prajitura):
    return f'ID={get_id(prajitura)}, nume={get_nume(prajitura)}, descriere={get_descriere(prajitura)}'\
        f' pret={get_pret(prajitura)}, nr_calorii={get_nr_calorii(prajitura)}, an_introducere_in_meniu={get_an_introducere(prajitura)}'



