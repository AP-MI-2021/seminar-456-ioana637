from Domain.prajitura import to_str
from Logic.crud import add_prajitura
from Logic.operatiuni import reducere_calorii

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


def run_crud_ui(prajituri):
    '''

    :param prajituri: lista de prajituri
    :return:
    '''

    def handle_show_all(prajituri):
        '''
        Afisare lista de prajituri din memorie
        :param prajituri: lista de prajitur
        :return:
        '''
        for prajitura in prajituri:
            print(to_str(prajitura))

    def handle_add_prajitura_ui(prajituri):
        '''
        Adaugam o prajitura citita de la tastatura in lista de prajituri
        :param prajituri: lista de prajituri
        :return:
        '''
        id = input('Dati idul prajiturii')
        nume = input('Dati numele')
        descriere = input('Dati descrierea')
        pret = float(input('Dati pretul'))
        nr_calorii = int(input('Dati numarul de calorii'))
        an_introducere = int(input('Dati anul introducerii in meniu'))
        add_prajitura(prajituri, id, nume, descriere, pret, nr_calorii, an_introducere)
        print('Prajitura a fost adaugata cu succes')

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_prajitura_ui(prajituri)
        elif cmd == '4':
            handle_show_all(prajituri)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida")


def run_operatiuni_ui(prajituri):
    '''

    :param prajituri: lista de prajituri
    :return:
    '''

    def handle_reducere_calorii(prajituri):
        '''
        Reducerea nr de calorii pentru prajiturile ce contin un string dat de la tastatura
        Cu cat se reduc caloriile se citeste de asemenea de la tastatura
        :param prajituri: lista de prajituri
        :return:
        '''
        reducere = int(input("Dati reducerea de calorii"))
        string_cautare = input("Dati stringul de cautare")
        reducere_calorii(prajituri, string_cautare, reducere)


    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_reducere_calorii(prajituri)
        elif cmd == '6':
            break
        else:
            print("Comanda invalida")



def run_undo_redo_ui(prajituri):
    pass


def run_console(prajituri):
    '''

    :param prajituri: lista de prajituri
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(prajituri)
        elif cmd == '2':
            run_operatiuni_ui(prajituri)
        elif cmd == '3':
            run_undo_redo_ui(prajituri)
        elif cmd == 'x':
            print("La revedere!")
            break
        else:
            print('Comanda invalida')
