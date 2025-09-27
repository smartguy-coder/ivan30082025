import requests
from pprint import pprint

# url = "https://www.ukr.net/news/politics.html"
#
# response = requests.get(url)
#
# print(response)
# # print(response.content)
# print(response.text)

url = 'https://dummyjson.com/todos'

params = {
    "limit": 1000,
    "skip": 0
}

response = requests.get(url, params=params)

# pprint(response.json())
response_json = response.json()
# pprint(response_json)

todos = response_json['todos']
pprint(todos)

uncompleted_todos = []
# uncompleted_todos_counter = 0
todos_user_id_69 = []

for todo in todos:
    if todo['userId'] == 69:
        todos_user_id_69.append(todo)

    if not todo['completed']:
        print(todo)
        uncompleted_todos.append(todo['todo'])
        # uncompleted_todos_counter += 1
pprint(uncompleted_todos)
# print(f'{uncompleted_todos_counter=}')

uncompleted_todos_counter2 = len(uncompleted_todos)
print(f'{uncompleted_todos_counter2=}')


pprint(todos_user_id_69)
