import datetime
from threading import Thread
from requests import sessions
from rocketchat_API.rocketchat import RocketChat
import json, time, random

# all
file_name_users_registered = 'users_registered_13_07_2022.txt'
server_url = 'https://rocket-chat.example.org'

# upload_file_to_room
room_id = 'r5puyEqPeohwpn4LT'
file_to_upload = 'test.docx'

with open(file_name_users_registered) as f:
    data = f.read()
users_dict = json.loads(data)

time_start = datetime.datetime.now()

login_count = 0
upload_files_count = 0
send_message_count = 0

def login_logout_users():
    global login_count
    while True:
        with sessions.Session() as session:
            i = random.choice(list(users_dict.items()))
        rocket = RocketChat(server_url=server_url)
        if rocket.login(i[0], i[1]).status_code == 200:
            print(f'User {i[0]} login success!')
            login_count += 1
        time.sleep(random.randint(1, 3))
        if rocket.logout().status_code == 200:
            print(f'User {i[0]} logout success!')
        time.sleep(random.randint(1, 3))

def send_test_message():
    global login_count, send_message_count
    while True:
        with sessions.Session() as session:
            i = random.choice(list(users_dict.items()))
        rocket = RocketChat(server_url=server_url)
        rocket.login(i[0], i[1])
        login_count += 1
        if rocket.chat_post_message(f'test message {i[0]}!', channel='tests').status_code == 200:
            print(f'User {i[0]} send_test_message success!')
            send_message_count += 1
        time.sleep(random.randint(1, 2))

def upload_file_to_room():
    global login_count, upload_files_count
    while True:
        with sessions.Session() as session:
            i = random.choice(list(users_dict.items()))
        rocket = RocketChat(server_url=server_url)
        rocket.login(i[0], i[1])
        login_count += 1
        if rocket.rooms_upload(room_id, file_to_upload).status_code == 200:
            print(f'User {i[0]} upload file success!')
            upload_files_count += 1
        time.sleep(random.randint(6, 20))


def send_stats():
    while True:
        time.sleep(10)
        time_works = datetime.datetime.now() - time_start
        print(f'''


        Load test working time: {time_works} 

        login_count = {login_count}
        upload_files_count = {upload_files_count}
        send_message_count = {send_message_count}
        ''')
login_logout_users()
if __name__ == '__main__':
    print("START")
    Thread(target=login_logout_users).start()
    Thread(target=send_test_message).start()
    Thread(target=upload_file_to_room).start()
    Thread(target=send_test_message).start()
    Thread(target=send_test_message).start()
    Thread(target=upload_file_to_room).start()
    Thread(target=send_stats).start()
    Thread(target=send_test_message).start()
    Thread(target=send_test_message).start()
    Thread(target=send_test_message).start()
    Thread(target=login_logout_users).start()
    Thread(target=send_test_message).start()
    Thread(target=upload_file_to_room).start()
    Thread(target=send_test_message).start()
    Thread(target=send_test_message).start()
    Thread(target=send_test_message).start()
