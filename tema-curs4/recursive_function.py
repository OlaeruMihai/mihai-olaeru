def recursive_function(*args, **kwargs):
    total_sum = 0
    even_sum = 0
    odd_sum = 0
    for i in args or kwargs:
        if type(i) == int:
            total_sum += i
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return total_sum, even_sum, odd_sum


print(recursive_function(1, 2, 7, 9, 12, 13))
