def validate_prajitura(id, nume, descriere, pret, calorii, an_introducere):
    '''
    Validate params for a prajitura/cake
    Throws a ValueError if fields are not correct
    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param calorii:
    :param an_introducere:
    :return:
    '''
    errors = []
    if id == '':
        errors.append('Id-ul nu poate fi vid')
    if nume == '':
        errors.append('Numele nu poate fi vid')
    if descriere == '':
        errors.append('Descrierea nu poate fi vid')
    try:
        pret = float(pret)
        if pret < 0:
            errors.append('Pretul trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append("Pretul trebuie sa fie un numar real")

    try:
        calorii = int(calorii)
        if calorii < 0:
            errors.append('Numarul de calorii trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append("Numarul de calorii trebuie sa fie un numar intreg")

    try:
        an_introducere = int(an_introducere)
        if an_introducere < 0:
            errors.append('Anul introducerii in meniu trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append("Anul introducerii in meniu trebuie sa fie un numar intreg")

    if len(errors) != 0:
        raise ValueError(errors)

    return id, nume, descriere, pret, calorii, an_introducere
