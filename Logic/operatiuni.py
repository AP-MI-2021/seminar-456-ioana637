from Domain.prajitura import get_nr_calorii, get_nume, set_nr_calorii

def reducere_calorii(prajituri, string_de_cautare, reducere):
    '''
    Reducerea caloriilor prajiturilor care au in nume string_de_cautare
    :param prajituri: lista de prajituri
    :param string_de_cautare: string
    :param reducere: int
    :return:
    '''
    for prajitura in prajituri:
        if string_de_cautare in get_nume(prajitura):
            nr_calorii_redus = get_nr_calorii(prajitura) - reducere
            set_nr_calorii(prajitura, nr_calorii_redus)


