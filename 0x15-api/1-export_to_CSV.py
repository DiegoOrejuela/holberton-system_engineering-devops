#!/usr/bin/python3
""" Module - 0-gather_data_from_an_API"""

if __name__ == "__main__":
    import requests
    import csv
    from sys import argv

    r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": int(argv[1])})
    dict_text = r.json()

    r = requests.get("https://jsonplaceholder.typicode.com/users",
                     params={"id": int(argv[1])})
    username = r.json()[0]["username"]

    for dict in dict_text:
        dict["username"] = username
        del dict["id"]

    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for dict in dict_text:
            writer.writerow(dict)
