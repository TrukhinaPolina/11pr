class Restaurant:

    def __init__(self, n, t, r):
        self.name = n
        self.type = t
        self.rating = r

    def describe_restaurant(self):
        print(f"Название ресторана: {self.name}")
        print(f"Тип кухни: {self.type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print("Ресторан открыт")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг {self.name} обновился до {self.rating}")


newRestaurant = Restaurant('Рест', 'Итальянская кухня', 4.5)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
# task 2,3
Rest1 = Restaurant('Метрополь', 'авторское меню',4.6)
Rest2 = Restaurant('Коо', 'японскую кухня',3.7)
Rest3 = Restaurant('Блок', 'мясной ресторан',4.2)
Rest1.describe_restaurant()
Rest2.describe_restaurant()
Rest3.describe_restaurant()
newRestaurant.update_rating(5.0)
