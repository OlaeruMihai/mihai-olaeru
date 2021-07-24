list_numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(list_numbers)

list_numbers_ascending = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list_numbers_ascending.sort()
print(list_numbers_ascending)

list_numbers_descending = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list_numbers_descending.sort(reverse = True)
print(list_numbers_descending)

my_sliced_list_even = list_numbers_ascending[1::2]
print(my_sliced_list_even)

my_sliced_list_odd = list_numbers_ascending[::2]
print(my_sliced_list_odd)

my_sliced_list_multiples = list_numbers_ascending [2::3]
print(my_sliced_list_multiples)
