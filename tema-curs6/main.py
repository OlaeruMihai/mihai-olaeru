from fraction_class import MyFirstFractionClass
if __name__ == '__main__':
    my_fraction = MyFirstFractionClass(2, 5)
    print(my_fraction)

    first_fraction_addition = MyFirstFractionClass(1, 4)
    second_fraction_addition = MyFirstFractionClass(1, 2)
    resulted_fraction_addition = first_fraction_addition + second_fraction_addition
    print(resulted_fraction_addition)

    first_fraction_subtraction = MyFirstFractionClass(1, 4)
    second_fraction_subtraction = MyFirstFractionClass(1, 2)
    resulted_fraction_subtraction = first_fraction_subtraction - second_fraction_subtraction
    print(resulted_fraction_subtraction)

