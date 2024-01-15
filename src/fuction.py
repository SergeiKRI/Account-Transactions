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
        if s["state"] == "EXECUTED":
            ex_lst.append(s)
    return ex_lst

def sort_data(lst):
    '''
    Сортирует по дате операции
    :param lst: неотсортированный список
    :return: список по дате операции
    '''

    return sorted(lst, key=lambda data: data.get("date"))


if __name__=='__main__':
    lst = load_operations()
    sort_data(lst)












