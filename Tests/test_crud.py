from Logic.crud import add_prajitura
from Domain.prajitura import create_prajitura, get_id, get_nume, get_descriere, get_pret, get_nr_calorii, get_an_introducere


def test_add_prajitura():
    prajituri = []
    prajitura_adaugata = create_prajitura('12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    add_prajitura(prajituri, '12d', 'spumos', 'prajitura roz', 5.6, 1000, 1990)
    assert len(prajituri) == 1
    assert prajituri[0] == prajitura_adaugata
    assert get_id(prajituri[0]) == '12d'
    assert get_nume(prajituri[0]) == 'spumos'
    assert get_descriere(prajituri[0]) == 'prajitura roz'
    assert get_pret(prajituri[0]) == 5.6
    assert get_nr_calorii(prajituri[0]) == 1000
    assert get_an_introducere(prajituri[0]) == 1990

    add_prajitura(prajituri, '123', 'tort', 'desc', 10.5, 1500, 1994)
    prajitura_adaugata_2 = create_prajitura('123', 'tort', 'desc', 10.5, 1500, 1994)
    assert len(prajituri) == 2
    assert prajituri[0] == prajitura_adaugata
    assert prajituri[1] == prajitura_adaugata_2
