from item import Item
from phone import Phone


phone1 = Phone("samsung", 500, 5, 1)
# print(phone1.calculate_total_price())
# print(phone1.all)
item1 = Item("my_phone", 500)

# This will throw an exception as name length is greater than 10
# item1.name = "my_cell_phone"
# print(item1.name)

# Giving an prompt as we cant set price value. as its read only parameter.
# item1.price = 1000

item1.apply_increment(0.2)
print(item1.price)

'''
Note: 
4 principle of OOPS
Encapsulation : name attribute could not sent unless an until condition is followed
Abstraction : Its shows only necessary information & hide unnecessary information. i.e private method
Inheritance : Reuse the code across child code
polymorphism : single entity does know how to handle different situation for example len function for string 
                len function for list
'''