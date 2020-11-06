import requests

Base=" http://127.0.0.1:5000/"
response= requests.get(Base+"lookup/3")
print("request is get")
print(response.json())