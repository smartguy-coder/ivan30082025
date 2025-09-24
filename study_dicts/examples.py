# name = 'Alex'
# age = 15

another_student_data = {}
student_data = {
    "name": 'Alex22',
    "name": 'Alex223333',
    "age": 15,
    "5": 6666545785,
    "hobbies": ['soccer', "tennis"],
    5: 25,
    6: 36,
    'empty_value': None,
    # 'toy_car': 'HotWheels'
}

# get data from dict
name = student_data["name"]
print(name)

toy_car = student_data.get("toy_car")
print(toy_car)

# create new data in dict
student_data['address'] = 'Hreshchatyk'
print(student_data)

# update data in dict
new_address = 'Derybasivska'
student_data['address'] = new_address
print(student_data)

# delete item
current_address = student_data.pop('address')
print(current_address)
print(student_data)
friends = student_data.pop('friends', None)
print(friends)
print(student_data)

del student_data["5"]
# del student_data["5666666"]
print(student_data)


# update with another dict
music_school_student_data = {
    "age": 155,
    'instruments': ['violin', 'guitar']
}

# merge data
# with update existing
# student_data.update(music_school_student_data)
# student_data.update(
#     {
#         'instruments': music_school_student_data['instruments']
#     }
# )
#
# print(student_data)

# with create new dict
new_dict = student_data | music_school_student_data
print(new_dict)
print(student_data)
