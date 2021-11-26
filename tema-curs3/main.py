list_numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(list_numbers)

list_numbers.sort()
print('List numbers ascending', list_numbers)

list_numbers.sort(reverse = True)
print('List numbers descending', list_numbers)

list_numbers=list_numbers[::-1]
my_sliced_list_even = list_numbers[1::2]
print(my_sliced_list_even)

my_sliced_list_odd = list_numbers[::2]
print(my_sliced_list_odd)

my_sliced_list_multiples = list_numbers [2::3]
print(my_sliced_list_multiples)
