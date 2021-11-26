def my_int_function(*args, **kwargs):
    parameter_value = 0
    for i in args or kwargs:
        if type(i) == int:
            parameter_value += i
    return parameter_value


print(my_int_function(1, 2))