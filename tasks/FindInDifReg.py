def find_in_different_registers(words: list[str]):
    '''
    Функция принимает список строк; далее создаются еще два списка со словами только в нижнем и только в верхнем регистре.
    Далее определяется регистр слова, и оно добавляется в список register (но теперь все буквы слова одного регистра).
    В итоге просматривается количество одинаковых слов в каждом регистре и записывается ответ, содержащий уникальные знаечния.
    :param words: список слов с различным регистром
    :return: res: список слов, которые не повторяются в том же регистре
    '''
    lst_low = [i.lower() for i in words]
    lst_up = [i.upper() for i in words]
    res = []
    register = []
    for i in range(len(words)):
        if words[i] > lst_up[i]:
            register.append(lst_low[i])
        else:
            register.append(lst_up[i])

    for i in range(len(words)):
        if register.count(register[i]) == 1 and lst_low[i] not in res:
            res.append(lst_low[i])

    return res

print(find_in_different_registers(['МАМА', 'Мама', 'БРАТ', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']))