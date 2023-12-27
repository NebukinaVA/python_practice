def int_to_roman(num: int):
    '''
    Функция-конвертер integer в римское число.
    Полученное число разбивается на единицы, десятые, сотые, тысячные.
    Затем цикл проходится по разрядам и ищет их в заданном словаре.
    Если разряда в словаре нет, то число разбивается на множители, и снова поиск в словаре

    :param num: число в арабском формате
    :return: число в римском формате
    '''
    if 0 >= num or num >= 4000:
        return
    d = {1 : 'I', 4: 'IV', 5: 'V', 9: 'IX', 10 : 'X', 40: 'XL', 50 : 'L', 90 : 'XC', 100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}
    lst = list(map(int, str(num)))
    lst = [lst[i]*10**(len(lst)-i-1) for i in range(len(lst))]
    lst.reverse()
    roman = ''
    for i in range(len(lst)):
        if lst[i] in d:
            roman = d.get(lst[i]) + roman
        elif 0 < lst[i]//10**(i) < 4:
            m = lst[i]//10**(i)
            roman = d.get(10**i)*m + roman
        elif 5 < lst[i]//10**(i) < 9:
            m = lst[i]//10**(i) - 5
            roman = d.get(5*10 ** i) + d.get(10 ** i) * m + roman
    return roman
