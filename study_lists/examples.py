some_sentence = "I live in Odesa."
result = some_sentence.split()  # ['I', 'live', 'in', 'Odesa']
# print(result)

mates = [
    'Andrey',
    'Marta',
    "Alex",
]

big_list = [
    True,
    False,
    0,
    '',
    'khjh',
    [
        4324, 346573, 5345
    ],
    'lkhjkjhg'
]

products = ['bread', 'salt', 'milk', 'snikers', 'bounty']
print(products)

# for product in products:
#     print(product)
    # if product.startswith("b"):
    #     print(1111111111)

# print(999999999)

# first_product = products[0]
# print(first_product)
second_product = products[1]
print(second_product)
#
# last_product = products[-1]
# print(last_product)

# user_input = input('Enter numbers (via whitespaces): ')
# user_input_as_list = user_input.split()
# print(user_input_as_list)
#
# total_sum = 0
# for string_number in user_input_as_list:
#     number = float(string_number)
#     # total_sum = total_sum + number
#     total_sum += number
#     print(total_sum, "-------")

additional_products = ['water', "sugar"]
mom_product = 'pasta'

# add list to list
products.extend(additional_products)
print(products)

# add item to list
products.append(mom_product)
print(products)

# delete item
products.remove(second_product)
print(products)

# sorting
products.sort(reverse=True)
print(products)

# new_products = sorted(products, reverse=True)
# print(new_products)


# change item
products[0] = 'BANANA'
print(products)

products.insert(3, 'mars')
print(products)


#