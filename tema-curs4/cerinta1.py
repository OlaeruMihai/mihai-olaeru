def my_function(a, b, c, *args, **kwargs):
    return a + b + c


my_sum = my_function(1, 5, -3, 'abc', [12, 56, 'cad'])
print(my_sum)


def my_zero_return_function():
    return 0


my_zero_return_function()
print(my_zero_return_function())


def my_third_function(a, b, *args, **kwargs):
    return a + b


my_second_sum = my_third_function(2, 4, 'abc', param_1=2)
print(my_second_sum)









