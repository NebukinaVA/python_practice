import pandas as pd
import os

def average_age_by_position(csv_file: str = '../samples/employees.csv'):
    '''
    Работа с pandas и csv
    Функция считывает данные из cvs файла в датафрейм, группируем строки по должности и считаем среднее.
    Записываем полученный результат в словарь.


    :param csv_file: строка с относительным путём к cvs файлу
    :return: возвращает словарь, в котором ключами являются уникальные должности, а
    значениями — средний возраст сотрудников на каждой должности
    '''
    try:
        data = pd.read_csv(os.path.abspath(csv_file))

        grouped_data = data.groupby('Должность').mean().to_dict()
        d = dict(grouped_data['Возраст'])
        return d
    except Exception as ex:
        print('status code 400\n', f'{ "Невалидный файл" if len(ex.args)<2 else ex.args[1]}')

