def calculator(expression):
    try:
        result = eval(expression)  # Используем функцию eval для вычисления значения выражения
        return result
    except:
        return "Ошибка! Проверьте правильность введенного выражения."

# Пример использования
user_input = input("Введите математическое выражение: ")
result = calculator(user_input)
print("Результат:", result)
