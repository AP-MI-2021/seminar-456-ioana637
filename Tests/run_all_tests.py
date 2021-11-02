from Tests.domain_test import prajitura_test
from Tests.test_crud import test_add_prajitura, test_edit_prajitura, test_delete_prajitura
from Tests.operatiuni_test import test_reducere_calorii, test_ordonare_prajituri, test_suma_preturi_per_an_introducere, \
    test_undo, test_undo_redo


def run_all_tests():
    test_add_prajitura()
    test_edit_prajitura()
    test_delete_prajitura()
    # test_reducere_calorii()
    # test_ordonare_prajituri()
    # test_suma_preturi_per_an_introducere()
    prajitura_test()
    test_undo()
    test_undo_redo()