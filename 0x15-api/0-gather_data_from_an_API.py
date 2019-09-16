#!/usr/bin/python3
""" Module - 0-gather_data_from_an_API"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://jsonplaceholder.typicode.com/users",
                     params={"id": int(argv[1])})
    name = r.json()[0].get("name")

    r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": argv[1]})
    count_all_task = len(r.json())

    r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": argv[1], "completed": "true"})
    list_task_done = r.json()
    count_task_done = len(list_task_done)

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          count_task_done,
                                                          count_all_task))
    for task in list_task_done:
        print("     " + task.get("title"))
