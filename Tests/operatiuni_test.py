from Logic.crud import add_prajitura
from Logic.operatiuni import reducere_calorii
from Domain.prajitura import get_nr_calorii

def test_reducere_calorii():
    prajituri = []
    add_prajitura(prajituri, 'id1', 'n1', 'desc1', 5.6, 1000, 2019)
    add_prajitura(prajituri, 'id2', 'n2', 'desc2', 6.6, 1200, 2010)
    reducere_calorii(prajituri, '1', 100)
    assert len(prajituri) == 2
    assert get_nr_calorii(prajituri[0]) == 900
    assert get_nr_calorii(prajituri[1]) == 1200

    reducere_calorii(prajituri, 'n', 200)
    assert len(prajituri) == 2
    assert get_nr_calorii(prajituri[0]) == 700
    assert get_nr_calorii(prajituri[1]) == 1000

