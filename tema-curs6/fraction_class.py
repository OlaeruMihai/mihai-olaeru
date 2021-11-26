
class MyFirstFractionClass:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        return MyFirstFractionClass(new_num, new_den)

    def __sub__(self, other):
        new_num = self.numerator * other.denominator - self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        return MyFirstFractionClass(new_num, new_den)

