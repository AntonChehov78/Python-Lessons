ticket = int(input('Сколько нужно билетов :'))
full_pay = 0
for i in range(1, ticket + 1):
    age = int(input(f'Возраст посетителя {i}: '))
    if 18 <= age < 25:
        full_pay += 990
    elif age >= 25:
        full_pay += 1390
print(f"Сумма оплаты без скидки:{full_pay} руб.")
if ticket > 3:
    full_pay = int(full_pay/100*90)
    print(f"Сумма оплаты с учетом скидки:{full_pay} руб.")