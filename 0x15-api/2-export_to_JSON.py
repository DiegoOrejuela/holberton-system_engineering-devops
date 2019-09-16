#!/usr/bin/python3
""" Module - 2-export_to_JSON"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": int(argv[1])})
    list_dict = r.json()

    r = requests.get("https://jsonplaceholder.typicode.com/users",
                     params={"id": int(argv[1])})
    username = r.json()[0].get("username")

    for dict in list_dict:
        dict["task"] = dict.pop("title")
        dict["username"] = username
        dict.pop("userId")
        dict.pop("id")

    json_dict = {argv[1]: list_dict}

    with open('{}.json'.format(argv[1]), 'w', encoding="UTF-8") as jsonfile:
        str_json = json.dumps(json_dict)
        jsonfile.write(str_json)
