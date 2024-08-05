number_first = int(input("Введите первое число  для проверки: "))
number_second = int(input("Введите второе число  для проверки: "))
number_third = int(input("Введите третье число  для проверки: "))

if number_first == number_second == number_third:

    print("3")

elif (number_first == number_second != number_third or number_first == number_third != number_second or
      number_second == number_third != number_first):

    print("2")
else:
    number_second != number_third != number_first
    print("0")
