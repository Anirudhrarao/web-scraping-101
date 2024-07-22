import json
import requests


def get_todos(url: str) -> None:
    """
        get_todos func take url and gives you json format response
    """
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None 

todos = get_todos('https://jsonplaceholder.typicode.com/todos')
# print("GET /todos:", todos)

def get_todos_detail(todo_id:int, url: str) -> None:
    """ get todos detail func basically takes two arg called todo id and url and give response todo"""
    full_url = f"{url}/{todo_id}"
    response = requests.get(full_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None 

todos_details = get_todos_detail(1,'https://jsonplaceholder.typicode.com/todos')
# print("GET /todos:", todos_details)

def create_todos(title: str, url: str, completed: bool=False) -> None:
    "create todos func take title, completed and url and send payload data to the server"
    payload =  {
        "userId": 1,
        "title": "Nothing to do anirudhra",
        "completed": True
    }

    headers = {
    'Content-Type': 'application/json; charset=UTF-8'
    }
    response = requests.post(url, data=json.dumps(payload),headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
new_todo = create_todos(title="Learn Python", url='https://jsonplaceholder.typicode.com/todos')
# print("POST /todos:", new_todo)


def update_todos(todo_id:int, url: str) -> None:
    full_url = f"{url}/{todo_id}"
    payload = {
    'userId': 1,
    'title': 'Anirudhra rao',
    'completed': True
    }
    response = requests.put(full_url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None 

updated_todo = update_todos(1,'https://jsonplaceholder.typicode.com/todos')
print("PUT /todos:", updated_todo)