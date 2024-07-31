import requests

def check_status_code(url: str) -> None:
    """
        check status code will take url as input and handle response code 
    """
    response = requests.get(url)
    if response.status_code == 200:
        print("Request was successful!")
    elif response.status_code == 404:
        print("Resource not found.")
    else:
        print(f"Received status code {response.status_code}")


# check_status_code('https://jsonplaceholder.typicode.com/posts/1')
# check_status_code('https://jsonplaceholder.typicode.com/posts/999')


def inspect_headers(url: str) -> None:
    """
        Inspecting headers: seeing data of headers
    """
    response = requests.get(url)

    print("Response Headers: ")
    for key, value in response.headers.items():
        print(f'{key}: {value}')

# inspect_headers('https://jsonplaceholder.typicode.com/posts/1')

def handle_response_content(url: str) -> None:
    """
        Handling reponse content takes parameter url and return reponse on the basis of content type of api
    """
    response = requests.get(url)
    if response.headers['Content-type'] == 'application/json; charset=utf-8':
        print("Response JSON")
        print(response.json())
    else:
        print("Response Text:")
        print(response.text)

# handle_response_content('https://jsonplaceholder.typicode.com/posts/1')


def fetch_data_with_error_handling(url: str) -> None:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        print("Response JSON:")
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

fetch_data_with_error_handling('https://jsonplaceholder.typicode.com/posts/1')
fetch_data_with_error_handling('https://jsonplaceholder.typicode.com/posts/999')