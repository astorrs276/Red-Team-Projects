import os 
import requests

# Environment variable testing
'''
key = 'HOME'
value = os.getenv(key) 
print("Value of 'HOME' environment variable :", value) 

key = 'PUBLIC'
value = os.getenv(key) 
print("Value of 'PUBLIC' environment variable :", value)

path = os.path.join(os.getenv("PUBLIC"), "payload.exe")
print(path)
'''

# url request information testing
'''
url = "https://www.google.com/"
response = requests.get(url, stream=True)
response.raise_for_status()
print(response)
for chunk in response.iter_content(chunk_size=1024):
    print(chunk)
'''

