#!/usr/bin/python3
""" Module - 2-export_to_JSON"""

if __name__ == "__main__":
    import json
    import requests

    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    list_dict = r.json()

    r = requests.get("https://jsonplaceholder.typicode.com/users")
    count_users = len(r.json())
    username = r.json()[0].get("username")

    for dict in list_dict:
        dict["task"] = dict.pop("title")
        dict["username"] = username
        dict.pop("id")

    json_dict = {}
    list_task = []
    for user in range(count_users):
        list_task = []
        for dict in list_dict:
            if (user + 1) == dict.get("userId"):
                dict.pop("userId")
                list_task.append(dict)
        json_dict[str(user + 1)] = list_task

    with open('todo_all_employees.json', 'w', encoding="UTF-8") as jsonfile:
        str_json = json.dumps(json_dict)
        jsonfile.write(str_json)
