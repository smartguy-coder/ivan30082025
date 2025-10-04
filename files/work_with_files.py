# file = open('work_with_files.py')
# 1/000
# file.close()

# read
# with open("data.txt", encoding='utf-8') as file:
#     file_content = file.read()
#     file_content2 = file.read()
#     print(file_content2)

# file_content3 = file.read() error - file closed


# write
# with open("data1.txt", mode='w', encoding='utf-8') as file:
#     file.write('111111111111111111\n')
#     file.write('222222222222222222\n')
#     file.write('33333333333333333333\n')

# add data
# with open("data123.txt", mode='a', encoding='utf-8') as file:
#     file.write('fffffffffffffffffff\n')
#     file.write('jjjjjjjjjjjjjjjjjj\n')
#     file.write('llllllllllllllllllll\n')


students = input('My students')
students_list = students.split()

position = 1
with open("students.txt", mode='+a', encoding='utf-8') as file:
    print(students_list)
    for student in students_list:
        file.write(f'{position}. {student.title()}\n')
        position += 1

    file.write('===================================================\n')
