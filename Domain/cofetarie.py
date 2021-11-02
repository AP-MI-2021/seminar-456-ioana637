# undo: 1, 2, 3
# curent: 3 -> 3_prim
# redo:


# undo: [], [1, 2]
# curenta: [1, 2]
#
from copy import deepcopy


def create_cofetarie():
    # return [[], [[]]]
    return {
        'listaCurenta': [],
        'listaUndo': [[]],
        'listaRedo': []
    }

def get_lista_curenta(cofetarie):
    return cofetarie['listaCurenta']

def get_lista_undo(cofetarie):
    return cofetarie['listaUndo']

def get_lista_redo(cofetarie):
    return cofetarie['listaRedo']

def set_lista_curenta(cofetarie, newCurrentList):
    cofetarie['listaCurenta'] = newCurrentList

def adaugare_lista_undo(cofetarie):
    listaCurenta = get_lista_curenta(cofetarie)
    get_lista_undo(cofetarie).append(deepcopy(listaCurenta))

# functia se va apela pentru operatiile care modifica listaCurenta
def adaugare_lista_undo_and_clear_redo(cofetarie):
    adaugare_lista_undo(cofetarie)
    clear_redo(cofetarie)

def adaugare_lista_redo(cofetarie):
    listaCurenta = get_lista_curenta(cofetarie)
    get_lista_redo(cofetarie).append(deepcopy(listaCurenta))

def clear_redo(cofetarie):
    get_lista_redo(cofetarie).clear()
