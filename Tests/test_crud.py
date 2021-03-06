from Domain.cofetarie import create_cofetarie, get_lista_curenta
from Logic.crud import add_prajitura, edit_prajitura, find_prajitura, delete_prajitura
from Domain.prajitura import create_prajitura, get_id, get_nume, get_descriere, get_pret, get_nr_calorii, get_an_introducere


def test_add_prajitura():
    cofetarie = create_cofetarie()
    prajitura_adaugata = create_prajitura('12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    add_prajitura(cofetarie, '12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    prajituri = get_lista_curenta(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 1
    assert prajituri[0] == prajitura_adaugata
    assert get_id(prajituri[0]) == '12d'
    assert get_nume(prajituri[0]) == 'spumos'
    assert get_descriere(prajituri[0]) == 'prajitura roz'
    assert get_pret(prajituri[0]) == 5.6
    assert get_nr_calorii(prajituri[0]) == 1000
    assert get_an_introducere(prajituri[0]) == 1990

    add_prajitura(cofetarie, '123', 'tort', 'desc', 10.5, 1500, 1994)
    prajitura_adaugata_2 = create_prajitura('123', 'tort', 'desc', 10.5, 1500, 1994)
    assert len(prajituri) == 2
    assert prajituri[0] == prajitura_adaugata
    assert prajituri[1] == prajitura_adaugata_2


def test_edit_prajitura():
    cofetarie = create_cofetarie()
    p1 = create_prajitura('12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    p2 = create_prajitura('123', 'spumos2', 'prajitura roz2', 5.6, 1000, 1990)
    add_prajitura(cofetarie, '12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    add_prajitura(cofetarie, '123', 'spumos2', 'prajitura roz2', 5.6, 1000, 1990)
    prajituri = get_lista_curenta(cofetarie)
    assert len(prajituri) == 2
    edit_prajitura(cofetarie, '12d', 'spumos new', 'prajitura roz new', 7.0, 1200, 2000)
    assert len(prajituri) == 2
    p1_new = find_prajitura(prajituri, '12d')
    assert get_id(p1_new) == '12d'
    assert get_nume(p1_new) == 'spumos new'
    assert get_descriere(p1_new) == 'prajitura roz new'
    assert get_pret(p1_new) == 7.0
    assert get_nr_calorii(p1_new) == 1200
    assert get_an_introducere(p1_new) == 2000

    try:
        edit_prajitura(cofetarie, '12d', '', 'prajitura roz new', 'jhdfsj', '-2154', 2000)
        assert False
    except ValueError:
        assert True

def test_delete_prajitura():
    cofetarie = create_cofetarie()
    add_prajitura(cofetarie, '12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    add_prajitura(cofetarie, '123', 'spumos2', 'prajitura roz2', 5.6, 1000, 1990)
    p1 = create_prajitura('12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    p2 = create_prajitura('123', 'spumos2', 'prajitura roz2', 5.6, 1000, 1990)
    prajituri = get_lista_curenta(cofetarie)
    assert len(prajituri) == 2
    delete_prajitura(cofetarie, '12d')
    assert len(prajituri) == 1
    delete_prajitura(cofetarie, '12d456')
    assert len(prajituri) == 1







