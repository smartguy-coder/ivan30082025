print("Hello world!")

name = "Ivan"
surname = "Mashchenko"
smile = '⚙'
cats_name = ''
my_best_friend_birthday = "20.01.2000"
string_number = "2"
poem = """
Як умру, то "поховайте"
Мене на могилі
Серед степу 'широкого'
На Вкраїні милій,
Щоб лани широкополі,
І Дніпро, і кручі
Було видно, було чути,
Як реве ревучий.
Як понесе з України
У синєє море
Кров ворожу... отойді я
І лани і гори —
Все покину, і полину
"""

difficult_string = """Я хочу мати одинарні лапки типу 'так', та подвійні лапки типу "інакше"! {}"""
something = "something"

print('here is the result', name, surname)
# print(poem)

# operations with strings
# 1 - зєднати стрічки
full_name = name + " " + surname
print(full_name)
full_name_with_smile = f"{name} {surname} {smile}"
full_name_with_smile = f"{name=} {surname=} {smile}"
print(full_name_with_smile)

full_name = 'nvcgfgfgfgg'
print(full_name)

# 2 множимо стрічки
some_string = "-=-"
header = some_string * 10
print(header)

# 3 інші операції
teacher = '       vasja 66 kartychak   '
teacher = teacher.title()
print(teacher)
teacher = teacher.strip()
print(teacher)
teacher = teacher.replace('66 ', '')
print(teacher)

teacher = teacher.replace('k', 'k!')
print(teacher)
teacher = teacher.replace('V', '000000000')
print(teacher)

# введення текстових даних
user_name = input("Введіть ваше імя: ")
message = f"Введено імя = {user_name}"
print(message)
