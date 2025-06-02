import requests
url='https:rcw-api-project-e5a2d9apcsfefuhu.canadacentral-01.azurewebsites.net/test'
response=requests.get(url)
reponse=response.json()
print(response['message'])
