# coding=utf-8
class Calculater(object):
    def add(self, num1, num2):
        return num1 + num2

    def devide(self, num1, num2):
        return num1 / num2

    def subtract(self, num1, num2):
        return num1 - num2


if __name__ == "__main__":
    calculat = Calculater()
    print(calculat.add(12, 21))
    print(calculat.subtract(12, 21))
    print(calculat.devide(12, 21))
