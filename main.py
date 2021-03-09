#exercise 1
my_list = ['howdy', 'hey', 'hi']
my_tuple = ('hello', 'hello', 'goodbye')
my_float = 86.45
my_int = int(86.45)
from decimal import Decimal
my_decimal = Decimal(86.45)
my_dict = {
    "name": "makenna",
    "age": 20
}

#exercise 2
import math
my_new_float = math.ceil(my_float)
print(my_new_float)

#exercise 3
my_sq_root = math.sqrt(my_float)
print(my_sq_root)

#exercise 4
my_first_el = my_dict["name"]
print(my_first_el)

#exercise 5
my_first_tuple = my_tuple[0]
print(my_first_tuple)

#exercise 6
my_list.append('hello')
print(my_list)

#exercise 7
my_list.pop(0)
my_list.insert(0, 'heyho')
print(my_list)

#exercise 8
my_list.sort
print(my_list)

#exercise 9
my_tuple += ('ciao',)
