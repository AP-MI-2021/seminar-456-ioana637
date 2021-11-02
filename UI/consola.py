from Domain.cofetarie import get_lista_curenta
from Domain.prajitura import to_str
from Logic.crud import add_prajitura, edit_prajitura
from Logic.operatiuni import reducere_calorii, apply_undo, apply_redo


def print_meniu_undo_redo():
    print('''
    MENIU -Undo/ Redo
    1. Undo 
    2. Redo
    3. Inapoi
    ''')

def print_meniu():
    print('''
    MENIU
    1. CRUD 
    2. Operatiuni
    3. Undo/Redo
    x. Iesire
    ''')

def print_crud_meniu():
    print('''
    MENIU Crud
    1. Adaugare
    2. Modificare
    3. Stergere
    4. Afisare toate prajiturile
    5. Inapoi
    ''')

def print_operatiuni_meniu():
    print('''
    MENIU Operatiuni
    1. Reducerea nr de calorii pentru toate prăjiturile care conțin în nume un string dat.
    2. Afișarea tuturor prăjiturilor introduse începând cu un an dat.
    3. Determinarea prăjiturii cu cel mai mare număr de calorii din fiecare an al introducerii.
    4. Ordonarea prăjiturilor crescător după raportul preț / calorii.
    5. Afișarea sumelor prețurilor pentru fiecare an al introducerii.
    6. Inapoi
    ''')


def run_crud_ui(cofetarie):
    '''

    :param prajituri: lista de prajituri
    :return:
    '''

    def handle_show_all(cofetarie):
        '''
        Afisare lista de prajituri din memorie
        :param prajituri: lista de prajitur
        :return:
        '''
        prajituri = get_lista_curenta(cofetarie)
        for prajitura in prajituri:
            print(to_str(prajitura))

    def handle_edit_prajitura_ui(cofetarie):
        '''
        Adaugam o prajitura citita de la tastatura in lista de prajituri
        :param prajituri: lista de prajituri
        :return:
        '''
        id = input('Dati idul prajiturii pe care vreti sa o editati')
        nume = input('Dati numele')
        descriere = input('Dati descrierea')
        pret = input('Dati pretul')
        nr_calorii = input('Dati numarul de calorii')
        an_introducere = input('Dati anul introducerii in meniu')
        try:
            edit_prajitura(cofetarie, id, nume, descriere, pret, nr_calorii, an_introducere)
            print('Prajitura a fost modificata cu succes')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_add_prajitura_ui(cofetarie):
        '''
        Adaugam o prajitura citita de la tastatura in lista de prajituri
        :param prajituri: lista de prajituri
        :return:
        '''
        id = input('Dati idul prajiturii')
        nume = input('Dati numele')
        descriere = input('Dati descrierea')
        pret = input('Dati pretul')
        nr_calorii = input('Dati numarul de calorii')
        an_introducere = input('Dati anul introducerii in meniu')
        try:
            add_prajitura(cofetarie, id, nume, descriere, pret, nr_calorii, an_introducere)
            print('Prajitura a fost adaugata cu succes')
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')
        finally:
            pass
            # codul de aici se executa si daca a fost functia executata cu succes si si daca au aparut erori

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_prajitura_ui(cofetarie)
        if cmd == '2':
            handle_edit_prajitura_ui(cofetarie)
        elif cmd == '4':
            handle_show_all(cofetarie)
        elif cmd == '5':
            pass
        else:
            print("Comanda invalida")


def run_operatiuni_ui(cofetarie):
    '''

    :param prajituri: lista de prajituri
    :return:
    '''

    def handle_reducere_calorii(cofetarie):
        '''
        Reducerea nr de calorii pentru prajiturile ce contin un string dat de la tastatura
        Cu cat se reduc caloriile se citeste de asemenea de la tastatura
        :param prajituri: lista de prajituri
        :return:
        '''
        reducere = int(input("Dati reducerea de calorii"))
        string_cautare = input("Dati stringul de cautare")
        reducere_calorii(cofetarie, string_cautare, reducere)

    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
           handle_reducere_calorii(cofetarie)
        elif cmd == '6':
            pass
        else:
            print("Comanda invalida")



def run_undo_redo_ui(cofetarie):
    def handle_undo(cofetarie):
        apply_undo(cofetarie)
        print('Undo facut cu succes')

    def handle_redo(cofetarie):
        apply_redo(cofetarie)
        print('Redo facut cu succes')

    while True:
        print_meniu_undo_redo()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_undo(cofetarie)
        if cmd == '2':
            handle_redo(cofetarie)
        elif cmd == '3':
            pass
        else:
            print("Comanda invalida")


def run_console(cofetarie):
    '''

    :param prajituri: lista de prajituri
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(cofetarie)
        elif cmd == '2':
            run_operatiuni_ui(cofetarie)
        elif cmd == '3':
            run_undo_redo_ui(cofetarie)
        elif cmd == 'x':
            print("La revedere!")
        else:
            print('Comanda invalida')
