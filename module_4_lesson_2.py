def test_function():
    message = 'Я в функции test_function'
    def  inner_function():
        print('Я в функции inner_function')
        print('Я в области видимости функции test_function')
        print(message)
    inner_function()


# Вызываем функцию test_function
# Внутри её определяем функцию inner_function
# Потом вызываем её внутри test_function
test_function()

# Функция не определена
# NameError: name 'inner_function' is not defined.
# Did you mean: 'test_function'?
# inner_function()