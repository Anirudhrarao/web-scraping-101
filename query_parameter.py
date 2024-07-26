import requests


def access_params(url: str) -> dict:
    """"
        access parmas takes url and return params from url
    """
    params = {'userId':1}
    response = requests.get(url,params=params)
    return response.url.split('?')[1]
    
params = access_params('https://jsonplaceholder.typicode.com')
# print('Params: ', params)

def fetch_post_by_user(base_url: str, user_id: int) -> None:
    query_params = {
        'userId': user_id
    }
    url = f"{base_url}/posts"
    try:
        response = requests.get(url, query_params)
        response.raise_for_status()
        posts = response.json()
        for post in posts:
            print(f'Post ID: {post['id']}, Title: {post['title']}')
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# fetch_post_by_user('https://jsonplaceholder.typicode.com',user_id=1)


def fetch_posts_by_multipler_user_ids(url: str, user_ids: list[int]) -> None:
    query_params = {
        'userId': user_ids
    }
    url = f"{url}/posts"
    try:
        response = requests.get(url,query_params)
        response.raise_for_status()
        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, User ID: {post['userId']}, Title: {post['title']}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

fetch_posts_by_multipler_user_ids('https://jsonplaceholder.typicode.com',user_ids=[1, 2])