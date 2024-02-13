def sum_of_square_digits(number, degree):
    index = 0
    str_number = str(number)
    count_symbol = len(str_number)
    happy_number = 0
    new_symbol = 0
    while (index < count_symbol):
        symbol = pow(int((str_number)[index]), degree)
        index = index + 1
        happy_number = int(symbol) + int(new_symbol)
        new_symbol = happy_number
    return(happy_number)

def is_happy_number(number):
    degree = 2
    iteration = 0
    count_iteration = 10
    happy_number = 0
    while ((iteration < count_iteration) and (happy_number != 1)):
        happy_number = sum_of_square_digits(number, degree)
        iteration = iteration + 1
        number = happy_number
    if happy_number == 1:
        return('true')
    else:
        return('false')

number = input("Введите число для проверки ")
print(is_happy_number(number))
