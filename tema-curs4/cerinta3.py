def my_last_function(*args, **kwargs):
    the_value_is = 0
    for i in args:
        if type(i) in [int]:
            the_value_is += i
    return the_value_is


print(my_last_function(5))