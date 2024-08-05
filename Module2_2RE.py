number_first = int(input("Введите первое число  для проверки: "))
number_second = int(input("Введите второе число  для проверки: "))
number_third = int(input("Введите третье число  для проверки: "))
if number_first == number_second == number_third:
    print("3")

if number_first == number_second != number_third:
    print("2")

if number_first != number_second != number_third:
    print("0")
