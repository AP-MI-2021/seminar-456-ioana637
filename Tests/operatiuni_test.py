from Logic.crud import add_prajitura
from Logic.operatiuni import reducere_calorii, sort_prajituri
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

