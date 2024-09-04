my_dict={'Aleksey':1988,'Oleg':1986,'Kostia':2001}
print(my_dict)
print(my_dict.get('Oleg'))
print(my_dict.get('Dima'))
my_dict.update({'Kolia':2010,'Nikola':1701})
print(my_dict.pop('Oleg'))
print(my_dict)

my_set={1,1,2,3,5,'Aleksey','Oleg','Oleg'}
print(my_set)
my_set.update({109,506})
print(my_set)
my_set.discard(109)
print(my_set)