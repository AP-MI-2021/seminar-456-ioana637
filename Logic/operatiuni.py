from Domain.prajitura import *


def reducere_calorii(prajituri, string_de_cautare, reducere):
    '''
    Reducerea caloriilor prajiturilor care au in nume string_de_cautare
    :param prajituri: lista de prajituri
    :param string_de_cautare: string
    :param reducere: int
    :return:
    '''
    result = []
    for prajitura in prajituri:
        prajitura_new = create_prajitura(get_id(prajitura), get_nume(prajitura), get_descriere(prajitura),
                                         get_pret(prajitura), get_nr_calorii(prajitura), get_an_introducere(prajitura))
        if string_de_cautare in get_nume(prajitura):
            nr_calorii_redus = get_nr_calorii(prajitura) - reducere
            set_nr_calorii(prajitura_new, nr_calorii_redus)
        result.append(prajitura_new)
    return result

def sort_prajituri(prajituri):
    '''
    TODO
    :param prajituri:
    :return:
    '''
    # return sorted(prajituri, key=sorting_criteria)
    return sorted(prajituri, key = lambda prajitura: get_pret(prajitura)/get_nr_calorii(prajitura))

def sorting_criteria(prajitura):
    '''
    TODO
    :param prajitura:
    :return:
    '''
    return get_pret(prajitura)/get_nr_calorii(prajitura)