# from math import inf
# import fake_math as fm
# import true_math as tm

# импортируем из модуля fake_math функцию деления и назначаем ей короткое имя
from fake_math import  fake_divide as fd
# импортируем из модуля true_math функцию деления и назначаем ей короткое имя
from true_math import  true_divide as td

# отдаём данные на обработку в модуль fake_math
result1 = fd(69, 3)
result2 = fd(3, 0)

# отдаём данные на обработку в модуль true_math
result3 = td(49, 7)
result4 = td(15, 0)

# Выводим полученные результаты
print(result1)
print(result2)

print(result3)
print(result4)
