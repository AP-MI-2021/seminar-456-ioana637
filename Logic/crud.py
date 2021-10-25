from copy import deepcopy

from Domain.prajitura import *
from Logic.validator import validate_prajitura

def find_prajitura(prajituri, id):
    '''
    Find prajitura in prajituri with id
    If not found, we return None
    :param prajituri:
    :param id:
    :return:
    '''
    for prajitura in prajituri:
        if get_id(prajitura) == id:
            return prajitura
    return None

def edit_prajitura(prajituri, id, nume_new, descriere_new, pret_new, calorii_new, an_introducere_new):
    '''
    Editarea prajituri cu idul id si aruncarea unei erori ValueError in cazul in care fieldurile nu sunt
    corecte
    :param prajituri:
    :param id:
    :param nume_new:
    :param descriere_new:
    :param pret_new:
    :param calorii_new:
    :param an_introducere_new:
    :return:
    '''
    id, nume_new, descriere_new, pret_new, calorii_new, an_introducere_new = validate_prajitura(id, nume_new, descriere_new, pret_new, calorii_new, an_introducere_new)
    updated_list = deepcopy(prajituri)
    for prajitura in updated_list:
        if get_id(prajitura) == id:
            set_nume(prajitura, nume_new)
            set_descriere(prajitura, descriere_new)
            set_pret(prajitura, pret_new)
            set_an_introducere(prajitura, an_introducere_new)
            set_nr_calorii(prajitura, calorii_new)
    return updated_list


def add_prajitura(prajituri, id, nume, descriere, pret, calorii, an_introducere):
    '''
    Adaugam in memorie, in lista de prajituri o prajitura formata
    din fieldurile: id, nume, descriere, pret, calorii, an_introducere
    :param prajituri: lista de prajituri
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: string
    :param calorii: string
    :param an_introducere: string
    :return:
    '''

    id, nume, descriere, pret, calorii, an_introducere = validate_prajitura(id, nume, descriere, pret, calorii, an_introducere)
    prajitura = create_prajitura(id, nume, descriere, pret, calorii, an_introducere)
    return prajituri + [prajitura]

def delete_prajitura(prajituri, id):
    '''
    .... TODO
    :param prajituri:
    :param id:
    :return:
    '''
    result_list = [prajitura for prajitura in prajituri if check_id(prajitura, id)]
    return result_list

def check_id(prajitura, id):
    return get_id(prajitura)!=id
