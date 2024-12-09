def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5,"яблоко",1.15]
print_params(*values_list)

values_dict = {'a': 2, 'b': 'словарь', 'c': False}
print_params(**values_dict)


values_list_2 = [99, 'Список2' ]
print_params(*values_list_2, 42)