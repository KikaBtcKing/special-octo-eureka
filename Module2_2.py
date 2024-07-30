number = int(input("Введите число для проверки: "))
first = 123
second = 567
third = 789
if first == number:
    print("3")
elif second == number:
    print("3")
elif third == number:
     print("3")

number = int(input("Введите число для проверки: "))
first = 123
second = 567
third = 789
if first or second == number:
    print("2")
elif third == number:
    print("2")
number = int(input("Введите число для проверки: "))
first = 123
second = 567
third = 789
if first and second != number:
    print("0")
elif third != number:
    print("0")