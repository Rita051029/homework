
class Number1:
    test_number = 3

    def __init__(self, number, number_2):
        self._number1 = number
        self._number2 = number_2
        self.__test_number2 = 1

    def _privat_numbers(self, number_3):
        self.__number3 = number_3
        self.__number4 = 2
        self.__number34 = self.__number3 + self.__number4
        print(self.__number34)

class Number(Number1):

    def __printer(self):
        print(self._number1)
        print(self._number2)
        print(min(self._number1,self._number2))
        print(max(self._number1, self._number2))
        print(f"{min(self._number1,self._number2)} < {max(self._number1,self._number2)}")

number = Number(3, 4)
#number.__printer()
number2 = Number1(4, 2)
number2._privat_numbers(90)