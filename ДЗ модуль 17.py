per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вложения"))
deposit = []
for key in per_cent:
        deposit.append(int(money * per_cent[key]/100 ))
print("Deposit:", deposit)
max_element = max (deposit)
print("Максимальная сумма, которую вы можете заработать за год: ", max_element, "руб.")