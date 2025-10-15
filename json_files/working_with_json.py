import json

initial_dict = {"name": "Іван", 'age': 14, "hobbies": [], "isMarried": False, "additional_info": None}

# dict to string
dict_to_string = json.dumps(initial_dict, ensure_ascii=False)
print(dict_to_string)

# string to dict
string_to_dict = json.loads(dict_to_string)
print(string_to_dict)

# FILES
# dict into file
with open("student.json", mode="w", encoding="utf-8") as target_file:
    json.dump(initial_dict, target_file, ensure_ascii=False, indent=4)

# with open("list.json", mode="w", encoding="utf-8") as target_file:
#     json.dump([{}, initial_dict], target_file, ensure_ascii=False, indent=4)

# read from file
with open("list.json", mode="r", encoding="utf-8") as target_file:
    content = json.load(target_file)
    print(content)