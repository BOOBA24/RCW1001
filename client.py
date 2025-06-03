import requests
url='https://rcw-api-project-e5a2d9apcsfefuhu.canadacentral-01.azurewebsites.net/'
response=requests.get(url)
data=response.json()
print(response['message'])
