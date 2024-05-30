
class Restaurant:

    def __init__(self, n, t, o):
        self.name = n
        self.type = t
        self.open = o

    def update_rating(self, new_rating):
        self.rating = new_rating


res1 = Restaurant("Рест", "Итальянская кухня", "работают с 10:00 до 23:00")
print(res1.name, res1.type, res1.open)
# task 2
Rest1 = Restaurant('Метрополь', 'авторское меню', 'с 11:00 до 00:00')
Rest2 = Restaurant('Коо', 'японскую кухня', 'с 14:00 до 02:00')
Rest3 = Restaurant('Блок', 'мясной ресторан', 'с 9:00 до 01:00')
print(Rest1.name, Rest1.type, Rest1.open)
print(Rest2.name, Rest2.type, Rest2.open)
print(Rest3.name, Rest3.type, Rest3.open)