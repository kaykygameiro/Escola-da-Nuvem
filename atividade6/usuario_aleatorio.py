import requests
import random

user_id = random.randint(1, 10)

try:
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    if response.status_code == 200:
        user = response.json()
        print(f"Nome: {user['name']}")
        print(f"E-mail: {user['email']}")
        print(f"País: {user['address']['city']}")
    else:
        print("Falha na conexão")
        
except:
    print("Falha na conexão")