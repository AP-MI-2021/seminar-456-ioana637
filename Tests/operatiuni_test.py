from Domain.cofetarie import create_cofetarie, get_lista_curenta, get_lista_undo, get_lista_redo
from Logic.crud import add_prajitura, delete_prajitura, edit_prajitura, find_prajitura
from Logic.operatiuni import reducere_calorii, sort_prajituri, compute_sum_prices_per_year, apply_undo, apply_redo
from Domain.prajitura import get_nr_calorii, create_prajitura


def test_reducere_calorii():
    prajituri = []
    prajituri = add_prajitura(prajituri, 'id1', 'n1', 'desc1', 5.6, 1000, 2019)
    prajituri = add_prajitura(prajituri, 'id2', 'n2', 'desc2', 6.6, 1200, 2010)
    prajituri = reducere_calorii(prajituri, '1', 100)
    assert len(prajituri) == 2
    assert get_nr_calorii(prajituri[0]) == 900
    assert get_nr_calorii(prajituri[1]) == 1200

    prajituri = reducere_calorii(prajituri, 'n', 200)
    assert len(prajituri) == 2
    assert get_nr_calorii(prajituri[0]) == 700
    assert get_nr_calorii(prajituri[1]) == 1000

def test_ordonare_prajituri():
    p1 = create_prajitura('id2', 'n1', 'desc1', 15.8, 200, 2019)
    p2 = create_prajitura('id2', 'n1', 'desc1', 7.6, 1000, 2019)
    p3 = create_prajitura('id1', 'n1', 'desc1', 5.6, 1000, 2019)

    sorted_list = sort_prajituri([p1,p2,p3])
    assert sorted_list[0] == p3
    assert sorted_list[1] == p2
    assert sorted_list[2] == p1

def test_suma_preturi_per_an_introducere():
    prajituri = []
    prajituri = add_prajitura(prajituri, 'id1', 'n1', 'desc1', 5.6, 1000, 2019)
    prajituri = add_prajitura(prajituri, 'id2', 'n2', 'desc2', 6.6, 1200, 2010)
    prajituri = add_prajitura(prajituri, 'id3', 'n3', 'desc3', 6.6, 1000, 2010)
    prajituri = add_prajitura(prajituri, 'id4', 'n4', 'desc4', 5.6, 700, 2010)

    suma_preturi_per_an_introducere = compute_sum_prices_per_year(prajituri)
    assert round(suma_preturi_per_an_introducere[2019],1) == 5.6
    assert round(suma_preturi_per_an_introducere[2010],1) == 18.8


def test_undo():
    cofetarie = create_cofetarie()
    add_prajitura(cofetarie, 'id1', 'n1', 'desc1', 5.6, 1000, 2019)
    add_prajitura(cofetarie, 'id2', 'n2', 'desc2', 6.6, 1200, 2010)
    assert len(get_lista_curenta(cofetarie)) == 2
    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 1
    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 0
    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 0

    add_prajitura(cofetarie, 'id1', 'n1', 'desc1', 5.6, 1000, 2019)
    add_prajitura(cofetarie, 'id2', 'n2', 'desc2', 6.6, 1200, 2010)
    delete_prajitura(cofetarie, 'id1')
    assert len(get_lista_curenta(cofetarie)) == 1
    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2

    edit_prajitura(cofetarie, 'id2', 'new', 'desc2new', 100.2, 1200, 2010)
    assert len(get_lista_curenta(cofetarie)) == 2
    assert find_prajitura(get_lista_curenta(cofetarie), 'id2') == create_prajitura('id2', 'new', 'desc2new', 100.2, 1200, 2010)
    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2
    assert find_prajitura(get_lista_curenta(cofetarie), 'id2') == create_prajitura('id2', 'n2', 'desc2', 6.6, 1200, 2010)

def test_undo_redo():
    cofetarie = create_cofetarie()

    add_prajitura(cofetarie, 'id1', 'n1', 'desc1', 5.6, 1000, 2019)
    add_prajitura(cofetarie, 'id2', 'n2', 'desc2', 6.6, 1200, 2010)
    add_prajitura(cofetarie, 'id3', 'n3', 'desc3', 2.6, 1000, 2019)
    assert len(get_lista_curenta(cofetarie)) == 3

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 1

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 0

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 0

    add_prajitura(cofetarie, 'id4', 'n1', 'desc1', 5.6, 1000, 2019)
    add_prajitura(cofetarie, 'id5', 'n2', 'desc2', 6.6, 1200, 2010)
    add_prajitura(cofetarie, 'id6', 'n3', 'desc3', 2.6, 1000, 2019)
    assert len(get_lista_curenta(cofetarie)) == 3

    apply_redo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 3

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 1

    apply_redo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2

    apply_redo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 3

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2
    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 1

    add_prajitura(cofetarie, 'id7', 'n3', 'desc3', 2.6, 1000, 2019)
    assert len(get_lista_curenta(cofetarie)) == 2
    apply_redo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 1

    apply_undo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 0
    apply_redo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 1
    apply_redo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2
    apply_redo(cofetarie)
    assert len(get_lista_curenta(cofetarie)) == 2








