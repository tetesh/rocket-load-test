from requests import sessions
from rocketchat_API.rocketchat import RocketChat
from datetime import date
import json

admin_login = 'aaddd'
admin_password = 'ddddddd'
server_url = 'https://rocket-chat.example.org'
mail_suffix = "@example.org"

password_users = 'testPa$$wd!123'
users = []
for i in range(1, 51):
    users.append(f'test_user_{i}')

def register_users(list_user, password_users, mail_suffix):
    users_registered = {}
    with sessions.Session() as session:
        rocket = RocketChat(admin_login, admin_password, server_url=server_url, session=session)
        for i in list_user:
            rocket.users_create(f'{i}{mail_suffix}', i, password_users, i)
            print(f'User {i} created')
            users_registered[i] = password_users
    return users_registered

x = register_users(users, password_users, mail_suffix)
print(x)

with open(f'users_registered_{date.today().strftime("%d_%m_%Y")}.txt', 'w') as fp:
    fp.write(json.dumps(x))
    print('Users registered safe to file')

