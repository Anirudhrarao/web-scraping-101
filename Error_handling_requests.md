### Error Handling with the `requests` Module

#### Common Exceptions

- **`requests.exceptions.RequestException`**: The base class for all exceptions raised by the `requests` module. Catching this will catch all exceptions related to requests.

- **`requests.exceptions.HTTPError`**: Raised for HTTP errors (e.g., 4xx or 5xx status codes).

- **`requests.exceptions.ConnectionError`**: Raised when there is a network problem (e.g., DNS failure, refused connection).

- **`requests.exceptions.Timeout`**: Raised when a request times out.

- **`requests.exceptions.TooManyRedirects`**: Raised when a request exceeds the configured number of maximum redirections.

-  **`response.raise_for_status()`**: This method checks the response status code and raises an `HTTPError` for 4xx or 5xx responses.


#### Basic Error Handling Example

Here’s a simple example of handling different types of exceptions:

```python
import requests

def fetch_url(url: str) -> None:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        print("Response received:", response.text)
    
    except requests.exceptions.Timeout:
        print("The request timed out")
    
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
fetch_url('https://httpbin.org/status/500')  # This will trigger an HTTPError
```