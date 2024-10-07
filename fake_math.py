# определяем функцию деления

def fake_divide(first, second):
    if second == 0:
        result = 'Ошибка, делить на ноль нельзя!'
    else:
        result = first / second
    return result