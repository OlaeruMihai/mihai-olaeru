def recursive_function(n):
    if n == 0:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = recursive_function(n - 1)
    total_sum += n
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

    return total_sum, even_sum, odd_sum


print(recursive_function(9))
