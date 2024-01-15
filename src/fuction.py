import json

def load_operations():
    '''
    Возвращает список из json файла
    :return:
    '''
    with open('operations.json', "r", encoding="utf-8") as file:
        return json.load(file)

def is_exect(lst):
    '''
    Является ли операция выполненой
    :return: список выполненых - list
    '''
    ex_lst = []
    for s in lst:
        if s.get("state")== "EXECUTED":
            ex_lst.append(s)
    return ex_lst

def sort_data(lst):
    '''
    Сортирует по дате операции
    :param lst: неотсортированный список
    :return: список по дате операции
    '''
    app_data = []
    for data in lst:
        if data.get('date'):
            app_data.append(data)

    return sorted(app_data, key=lambda x: x.get("date"), reverse=True)

def form_data(date):
    '''
    Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)
    :param date: дата в формате ГГГГ-ММ-ДД
    :return:
    '''
    mod_date = date.split('-')
    return f'{mod_date[2][:2]}.{mod_date[1]}.{mod_date[0]}'

def mask_card(number):
    """
Номер карты в формате  XXXX XX** **** XXXX
Номер счета в формате  **XXXX
    :param number: str
    :return:
    """
    name_card = number.split(' ')
    if name_card[0] == 'Счет':
        return 'Счет **' + name_card[-1][-4:]

    else:
        form_card = name_card[-1][:6]+'******'+name_card[-1][-4:]
        # разбивает номер по 4 цифры
        num_ = [form_card[i:i+4] for i in range(0, len(form_card), 4)]

        return ' '.join(name_card[:-1] + num_)

def form_modif(dict_):
    '''
    Выводит в нужном формате
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
    :param dict_: dict
    :return: str
    '''
    return (f'{form_data(dict_["date"])} {dict_["description"]}\n'
            f'{mask_card(dict_.get("from"," "))} -> {mask_card(dict_["to"])}\n'
            f'{dict_["operationAmount"]["amount"]} {dict_["operationAmount"]["currency"]["name"]}\n')
