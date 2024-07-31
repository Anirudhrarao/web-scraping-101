import requests

def set_cookies(url: str) -> None:
    cookies = {
        'example_cookie' : 'Anirudhra cookies'
    }
    response = requests.get(url=url, cookies=cookies)
    if response.status_code == 200:
        return f"Cookie setted successfully {response.json()['cookies']['example_cookie']}"
    else:
        return "Cookie not setted"

# cookie = set_cookies('https://httpbin.org/cookies')
# print("Response JSON: ",cookie)



def get_cookies(url: str) -> None:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Cookies: {response.json()['cookies']['example_cookie']}')
    else:
        print('No cookies found!')

# url = 'https://httpbin.org/cookies/set/example_cookie/aniruddh'
# get_cookies(url)


def persist_cookies(url_set_cookie: str, url_get_cookie: str) -> None:
    session = requests.Session()
    # Request to set cookies
    response_set = session.get(url_set_cookie)
    if response_set.status_code == 200:
        print('Cookies set successfully')
    else:
        print('Cookies not set')
    
    # Request to get cookies
    response_get = session.get(url_get_cookie)
    if response_get.status_code == 200:
        print(f'cookies: {response_set.json()['cookies']['session_cookie']}')
    else:
        print('No cookies found')


# url_set_cookie = 'https://httpbin.org/cookies/set/session_cookie/anirudhra'

# url_get_cookie = 'https://httpbin.org/cookies'

# persist_cookies(url_set_cookie, url_get_cookie)


def login_and_get_profile():
    session = requests.Session()
    # Define the URL to set a cookie (simulate login)
    login_url = 'https://httpbin.org/cookies/set/session_cookie/session_value'
    response = session.get(login_url)
    if response.status_code == 200:
        print("Login simulation successful!")
        
        # Define the URL to retrieve cookies (simulate profile access)
        profile_url = 'https://httpbin.org/cookies'
        
        # Access the profile page with the session
        response = session.get(profile_url)
        if response.status_code == 200:
            print("Profile page accessed!")
            print(response.json())
        else:
            print(f"Failed to access profile page. Status code: {response.status_code}")
    else:
        print(f"Login simulation failed. Status code: {response.status_code}")

login_and_get_profile()