import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def fetch_with_timeout(url: str) -> None:
    """
        Amount of time that clien wait for a server to send response.
    """
    try:
        response = requests.get(url, timeout=5) 
    except requests.Timeout:
        print("The request timed out")
    except requests.RequestException as e:
        print("The request timed out")

# fetch_with_timeout('https://httpbin.org/delay/3')

def fetch_with_retries(url: str) -> None:
    session = requests.Session()

    # Defin strategy
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"],
        backoff_factor=1
    )

    # Mount adapter with retry strategy
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response = session.get(url)
        print("Response received:", response.text)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    
fetch_with_retries('https://httpbin.org/status/500')