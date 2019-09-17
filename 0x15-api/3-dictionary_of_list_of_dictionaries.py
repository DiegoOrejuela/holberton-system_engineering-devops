#!/usr/bin/python3
""" Module - 2-export_to_JSON"""

if __name__ == "__main__":
    import json
    import requests

    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    list_dict = r.json()

    r = requests.get("https://jsonplaceholder.typicode.com/users")
    users = r.json()

    for dict in list_dict:
        for user in users:
            if dict.get("userId") == user.get("id"):
                dict["username"] = user.get("username")
        dict["task"] = dict.pop("title")
        dict.pop("id")

    json_dict = {}
    for user in users:
        list_task = []
        for dict in list_dict:
            if user.get("id") == dict.get("userId"):
                dict.pop("userId")
                list_task.append(dict)
        json_dict[user.get("id")] = list_task

    with open('todo_all_employees.json', 'w', encoding="UTF-8") as jsonfile:
        str_json = json.dumps(json_dict)
        jsonfile.write(str_json)
