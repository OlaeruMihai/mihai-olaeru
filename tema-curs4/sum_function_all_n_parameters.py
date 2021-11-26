
def my_sum_function_n_parameters(*args, **kwargs):
    index_value = 0
    for i in args:
        if type(i) == int:
            index_value += i

    return index_value


print(my_sum_function_n_parameters(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_sum_function_n_parameters())
print(my_sum_function_n_parameters(2, 4, 'abc', param_1=2))
