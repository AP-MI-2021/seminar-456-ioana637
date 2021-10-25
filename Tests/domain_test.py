from Domain.prajitura import *

def prajitura_test():
    prajitura = create_prajitura('id', 'nume', 'descriere', 23.45, 240, 1999)
    assert get_id(prajitura) == 'id'
    assert get_nume(prajitura) == 'nume'
    assert get_descriere(prajitura) == 'descriere'
    assert get_pret(prajitura) == 23.45
    assert get_an_introducere(prajitura) == 1999
    assert get_nr_calorii(prajitura) == 240

    set_id(prajitura, 'id2')
    set_nume(prajitura, 'nume2')
    set_descriere(prajitura, 'descriere2')
    set_pret(prajitura, 50.5)
    set_an_introducere(prajitura, 1985)
    set_nr_calorii(prajitura, 300)

    assert get_id(prajitura) == 'id2'
    assert get_nume(prajitura) == 'nume2'
    assert get_descriere(prajitura) == 'descriere2'
    assert get_pret(prajitura) == 50.5
    assert get_an_introducere(prajitura) == 1985
    assert get_nr_calorii(prajitura) == 300
