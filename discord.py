from random import choice
import requests as r
import time
import random

s = r.Session()
s.headers['authorization'] = input('Token: ')
msg_set: list = open('msg.txt', 'r', encoding='utf-8').read().splitlines()
chat_id = input('Input chat id: ')
total_sent = 0


while True:
    msg = choice(msg_set)
    print(f'Sending message {msg}')
    _data = {'content': msg, 'tts': False}
    resp = s.post(
        f'https://discord.com/api/v9/channels/{chat_id}/messages', json=_data).json()
    msg_id = resp['id']
    total_sent += 1
    print(f'Message sent (Already {total_sent} in total).')
    delay = random.randint(150,350)
    print(f'Sleeping {delay} seconds')
    time.sleep(delay)