import json


class Raf9:
    def __init__(self):
        self.ingridients = ['lemon', 'soda', 'orange', 'ice']

    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input("Введите команду:")
            if command == '0':
                print("Всего доброго приходите еще!")
                break
            elif command == '1':
                current_ings = self.choose_ingridients()
                self.find_coctail(current_ings)
            else:
                print("Не знаю такой команды")


    def __help_text(self):
        print("Доступные команды:")
        print("1- выбрать ингредиент")
        print("0- выход")

    def get_coctails_from_db(self)
        with open('coctails.json', 'r') as json_file:
            self.coctails = json.load(json_file)
            pass

    def find_coctail(self, current_ings):
        pass

    def choose_ingridients(self):
        choosed_ingr = []
        print('Список ингредиентов')
        i = 0
        for ing in self.ingridients:
            i += 1
            print(f'{i}, {ing}')
        while True:
            command = input("Введите команду:")
            if command == '0':
                return choosed_ingr
            else:
                if command.isdigit():
                    number = int(command)
                    if number > len(self.ingridients):
                        print('Такого ингредиента в списке нет')
                    else:
                        choosed_ingr.append(self.ingridients[number-1])
                else:
                    print("Введите номер ингредиента")










if __name__ == '__main__':
    raf9 = Raf9()
    raf9()

