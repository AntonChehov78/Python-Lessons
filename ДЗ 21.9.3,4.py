class Client:
    def __init__(self, first_name,second_name,city, balance):
        self.first_name=first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def __str__(self):
        return f' "{self.first_name}, {self.second_name}. {self.city}. Баланс:{self.balance} руб." '
    def gosti(self):
        return f' "{self.first_name}, {self.second_name}. {self.city}" '
clients=Client ("Ivan", "Ivanov", "Moscow",5)
print(clients)

clients_1= Client("Ivan", "Ivanov", "Moscow", 5)
clients_2= Client("Artem", "Sidorov", "Samara", 10)
clients_3= Client("Olga", "Petrova", "Oslo", 15)

gosti_spisok=[clients_1, clients_2, clients_3]
for guest in gosti_spisok:
    print(guest.gosti())




