from requests import sessions
from rocketchat_API.rocketchat import RocketChat
from datetime import date
import json

admin_login = 'ssss'
admin_password = 'sssss'

file_name_users_registered = 'users_registered_13_07_2022.txt'
server_url = 'https://rocket-chat.example.org'

with open(file_name_users_registered) as f:
    data = f.read()
users_dict = json.loads(data)

def delete_users():
    with sessions.Session() as session:
        rocket = RocketChat(admin_login, admin_password, server_url=server_url, session=session)
    for i in users_dict:
        try:
            id_user = rocket.users_info(username=i).json()["user"]["_id"]
            if rocket.users_delete(user_id=id_user).status_code == 200:
                print(f"User {i} delete success!")
        except KeyError:
            print(f'User {i} not found')

if __name__ == '__main__':
    print("start delete users")
    delete_users()