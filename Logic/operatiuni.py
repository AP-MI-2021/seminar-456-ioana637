from Domain.cofetarie import get_lista_curenta, adaugare_lista_undo, get_lista_undo, set_lista_curenta, \
    adaugare_lista_redo, get_lista_redo, clear_redo, adaugare_lista_undo_and_clear_redo
from Domain.prajitura import *


def reducere_calorii(cofetarie, string_de_cautare, reducere):
    '''
    Reducerea caloriilor prajiturilor care au in nume string_de_cautare
    :param prajituri: lista de prajituri
    :param string_de_cautare: string
    :param reducere: int
    :return:
    '''
    # result = []
    # for prajitura in prajituri:
    #     prajitura_new = create_prajitura(get_id(prajitura), get_nume(prajitura), get_descriere(prajitura),
    #                                      get_pret(prajitura), get_nr_calorii(prajitura), get_an_introducere(prajitura))
    #     if string_de_cautare in get_nume(prajitura):
    #         nr_calorii_redus = get_nr_calorii(prajitura) - reducere
    #         set_nr_calorii(prajitura_new, nr_calorii_redus)
    #     result.append(prajitura_new)
    # return result

    adaugare_lista_undo_and_clear_redo(cofetarie)

    prajituri = get_lista_curenta(cofetarie)
    for prajitura in prajituri:
        if string_de_cautare in get_nume(prajitura):
            nr_calorii_redus = get_nr_calorii(prajitura) - reducere
            set_nr_calorii(prajitura, nr_calorii_redus)


def sort_prajituri(prajituri):
    '''
    TODO
    :param prajituri:
    :return:
    '''
    # return sorted(prajituri, key=sorting_criteria)
    return sorted(prajituri, key=lambda prajitura: get_pret(prajitura) / get_nr_calorii(prajitura))


def sorting_criteria(prajitura):
    '''
    TODO
    :param prajitura:
    :return:
    '''
    return get_pret(prajitura) / get_nr_calorii(prajitura)


def compute_sum_prices_per_year(prajituri):
    '''
    TODO
    :param prajituri:
    :return:
    '''
    result = {}
    for prajitura in prajituri:
        year = get_an_introducere(prajitura)
        price = get_pret(prajitura)
        if year in result:
            result[year] += price
        else:
            result[year] = price
    return result


def apply_undo(cofetarie):
    '''
    TODO
    :param cofetarie:
    :return:
    undo: []
    curenta: []
    undo: 1, 2, 3
    curenta: 1
    '''
    lista_undo = get_lista_undo(cofetarie)
    if len(lista_undo) > 1:
        adaugare_lista_redo(cofetarie)
        prior_lista_curenta = lista_undo.pop()
        set_lista_curenta(cofetarie, prior_lista_curenta)
    else:
        set_lista_curenta(cofetarie, [])


def apply_redo(cofetarie):
    '''
    TODO
    :param cofetarie:
    :return:
    '''
    lista_redo = get_lista_redo(cofetarie)
    if len(lista_redo) > 0:
        adaugare_lista_undo(cofetarie)
        new_current_list = lista_redo.pop()
        set_lista_curenta(cofetarie, new_current_list)
