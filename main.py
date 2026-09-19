import random
class shifr:

    def __init__(self, a, b):
        self._a = a
        self._b = b
        self._result = self.__calculate()

    def __calculate(self):
        operation = random.choice(["+", "-", "*", "/"])
        if operation == "+":
            return self._a + self._b
        elif operation == "-":
            return self._a - self._b
        elif operation == "*":
            return self._a * self._b
        elif operation == "/":
            return self._a / self._b

    def __str__(self):
        return str(self._result)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
shifr = shifr(num1, num2)
print(shifr)