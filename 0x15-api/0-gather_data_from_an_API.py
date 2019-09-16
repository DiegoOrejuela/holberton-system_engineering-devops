#!/usr/bin/python3
""" Module - 0-gather_data_from_an_API"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(argv[1]))
    name = r.json().get("name")

    r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": argv[1]})
    list_dict = r.json()
    count_all_task = len(list_dict)

    list_task_done = []
    for dict in list_dict:
        if dict.get("completed"):
            list_task_done.append(dict)

    count_task_done = len(list_task_done)

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          count_task_done,
                                                          count_all_task))
    for task in list_task_done:
        print("\t {}".format(task.get("title")))
