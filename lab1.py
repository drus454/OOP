from typing import Union
import doctest


class Rectangle:
    """
    Представление прямоугольника
    """
    def __init__(self, width: Union[int, float], height: Union[int, float]):
        """
        Иницилизация прямоугольника
        :param width: Ширина
        :param height: Высота
        >>> rectangle1 = Rectangle(10, 15)
        >>> rectangle2 = Rectangle(-10, 15)
        Traceback (most recent call last):
        ...
        ValueError: Ширина не может быть отрицательная или равна нулю
        >>> rectangle3 = Rectangle(10, -15)
        Traceback (most recent call last):
        ...
        ValueError: Высота не может быть отрицательная или равна нулю
        >>> rectangle4 = Rectangle('10', 15)
        Traceback (most recent call last):
        ...
        TypeError: Число должно быть int или float
        >>> rectangle5 = Rectangle(10, "15")
        Traceback (most recent call last):
        ...
        TypeError: Число должно быть int или float
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Число должно быть int или float")
        if width <= 0:
            raise ValueError("Ширина не может быть отрицательная или равна нулю")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Число должно быть int или float")
        if height <= 0:
            raise ValueError("Высота не может быть отрицательная или равна нулю")
        self.height = height

    def perimeter(self):
        """
        Вычисление периметра
        :return: Периметр
        >>> rectangle1 = Rectangle(10, 15)
        >>> rectangle1.area()
        150
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисление площади
        :return: Площадь
        >>> rectangle1 = Rectangle(10, 15)
        >>> rectangle1.perimeter()
        50
        """
        return self.width * self.height



class Calculator:
    """
    Базовый калькулятор
    """
    def __init__(self, par1, par2):
        """
        Калькулятор
        :param par1: Первое значение
        :param par2: Второе значение
        >>> a = Calculator('4', 5)
        Traceback (most recent call last):
        ...
        TypeError: Число должно быть int или float
        >>> b = Calculator(4, '5')
        Traceback (most recent call last):
        ...
        TypeError: Число должно быть int или float
        """

        if not isinstance(par1, (int, float)):
            raise TypeError("Число должно быть int или float")
        self.par1 = par1

        if not isinstance(par2, (int, float)):
            raise TypeError("Число должно быть int или float")
        self.par2 = par2


    def add(self):
        """
        Сложение чисел
        :return: Сумму
        >>> a = Calculator(4, 5)
        >>> a.add()
        9
        """
        return self.par1 + self.par2

    def subtraction(self):
        """
        Вычитание чисел
        :return: Вычитание
        >>> a = Calculator(4, 5)
        >>> a.subtraction()
        -1
        """
        return self.par1 - self.par2

    def multiplication(self):
        """
        Умножение чисел
        :return: Произведение
        >>> a = Calculator(4, 5)
        >>> a.multiplication()
        20
        """
        return self.par1 * self.par2

    def division(self):
        """
        Деление чисео
        :return: Деление
        >>> a = Calculator(10, 5)
        >>> a.division()
        2.0
        >>> b = Calculator(10, 0)
        >>> b.division()
        Traceback (most recent call last):
        ...
        ZeroDivisionError: На ноль делить нельзя
        """
        if self.par2 == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        return self.par1 / self.par2


class BankAccount:
    """
    Класс для представления банковского счета.
    """

    def __init__(self, account_number, balance=0):
        """
        Инициализация банковского счета.

        :param account_number: Номер счета.
        :param balance: Начальный баланс (по умолчанию 0).

        >>> account = BankAccount("123456")
        >>> account.account_number
        '123456'
        >>> account.balance
        0
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Внесение денег на счет.

        :param amount: Сумма для внесения.
        :return: Новый баланс после внесения.

        >>> account = BankAccount("123456", 100)
        >>> account.deposit(50)
        150
        >>> account.deposit(-50)
        Traceback (most recent call last):
        ...
        ValueError: Сумма для внесения должна быть положительной.
        """
        if amount < 0:
            raise ValueError("Сумма для внесения должна быть положительной.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия.
        :return: Новый баланс после снятия.

        >>> account = BankAccount("123456", 100)
        >>> account.withdraw(30)
        70
        >>> account.withdraw(100)
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно средств на счете.
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount
        return self.balance






if __name__ == "__main__":
    doctest.testmod()


