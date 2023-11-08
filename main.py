

class Number1:
    test_number = 3

    def __init__(self, number, number_2):
        self._number1 = number
        self._number2 = number_2
        self._number11 = 11
        self.__test_number2 = 1
        self.__test_number3 = 2

    def __privat_numbers(self, number_3):
        self.__number3 = number_3
        self.__number4 = 4
        self.__number34 = self.__number3 + self.__number4
        print(self.__number34)

    def _not_privat_numbers(self, number5):
        self._number5 = number5
        self._number6 = 6
        print(self._number5 - self._number6)

class Number(Number1):

    def __privat_numbers2(self, number7):
        self.__number7 = number7
        self.__number8 = 8
        print(self.__number7 - self.__number8 - self._number11)

    def _not_privat_numbers2(self, number9):
        self._number9 = number9
        self._number10 = 10
        print(self._number9 + self._number10 + self._number11)


number = Number(3, 4)
number._not_privat_numbers2(10)
number2 = Number1(4, 2)
number2._not_privat_numbers(90)