from src.function import *

list_test = [{
    "id": 441945886,
    "state": "EXECUTED"},
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689"},
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582"}
]


def test_is_exect():
    assert is_exect({}) == []
    assert is_exect(list_test) == [{"id": 441945886, "state": "EXECUTED"},
                                   {"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582"}]


def test_sort_data():
    assert sort_data(list_test) == [{"id": 863064926,
                                     "state": "EXECUTED",
                                     "date": "2019-12-08T22:46:21.935582"},
                                    {"id": 594226727,
                                     "state": "CANCELED",
                                     "date": "2018-09-12T21:27:25.241689"}
                                    ]
def test_form_data():
    assert form_data(list_test[1]['date']) == '12.09.2018'
    assert form_data(list_test[2]["date"]) == '08.12.2019'

def test_mask_card():
    assert mask_card('Счет 72731966109147704472') == 'Счет **4472'
    assert mask_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
    assert mask_card('') == ''

old_list = {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"}
def test_form_modif():
    assert form_modif(old_list) == ('08.12.2019 Открытие вклада\n'
                                    ' -> Счет **5907\n'
                                    '41096.24 USD\n')
