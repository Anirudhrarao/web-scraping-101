import requests

def upload_file(file_path: str, upload_url: str) -> None:
    with open(file_path, 'rb') as file:
        files = {
            'file' : file
        }

        response = requests.post(upload_url, files=files)   
        if response.status_code == 200:
            print('File uploaded successfully!')
            print('Response Json:', response.json())
        else:
            print(f"Failed to upload file, status code: {response.status_code}")
            print(response.text)

file_path = 'demo.txt'
upload_url = 'https://httpbin.org/post'
# upload_file(file_path, upload_url)

def upload_file(file_path: str, upload_url: str, additional_data: dict = None) -> None:
    with open(file_path, 'rb') as file:
        files = {
            'file' : file
        }

        response = requests.post(upload_url, files=files, data=additional_data)   
        if response.status_code == 200:
            print('File uploaded successfully!')
            print('Response Json:', response.text)
        else:
            print(f"Failed to upload file, status code: {response.status_code}")
            print(response.text)

file_path = 'demo.txt'
additional_data = {'user_id': '12345', 'description': 'Sample file upload'}
upload_url = 'https://httpbin.org/post'
upload_file(file_path, upload_url, additional_data)