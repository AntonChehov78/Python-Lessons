while True:
    some_numbers = input("Ввести несколько цифр, через пробел: ")
    try:
        structure = list(map(int, some_numbers.split()))
        if len(structure) < 2:
            print("По условию необходимо ввести не менее двух цифр")
        else:
            break
    except ValueError:
        print("Ошибка. Ввести несколько цифр, через пробел: ")
while True:
    try:
        one_number = int(input("Ввести любое число: "))
        break
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")
def structure_sort(structure):
    for i in range(1, len(structure)):
        a = structure[i]
        adx = i
        while adx > 0 and structure[adx - 1] > a:
            structure[adx] = structure[adx - 1]
            adx -= 1
        structure[adx] = a
    return structure
def numer_search(structure, one_number, left, right):
    pos = -1

    while left <= right:
        mid = (left + right) // 2

        if structure[mid] < one_number:
            left = mid + 1
        elif structure[mid] >= one_number:
            pos= mid
            right = mid - 1

    if pos != -1 and pos <= len(structure) - 1:
        return pos
    else:
        return -1
structure = structure_sort(structure)
index = numer_search(structure, one_number, 0, len(structure) - 1)
if index <= 0:
    print(f"Ввод числа {one_number} не соответствует задаче.")
elif index == -1:
    print(f"Ввод числа  {one_number} не соответствует задаче.")
else:
    print(
        f'Номер расположения цифры {index - 1}, это меньше введенного числа: {one_number} в списке {structure}.')
    print(f"Цифра больше или равна числу {one_number}, на позиции {index}.")
