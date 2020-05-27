import sys
from time import timezone

from datetime import datetime, date, time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime, timedelta
from datetime import time
import random

token = "3cbadf7754a4e2beaa1bd0ef9b6a9eb94d216f1bcba27ecd922aef1d7015a3707297271e9a403ed517531"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session,192117978)

#бля, создам ещё 1 версию чтобы всё на bot_longpoll было

def send_message(vk_session, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{'peer_id': id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})



def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    if response == 'здравствуйте':
        keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Какой сейчас урок?', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Хочу задать вопрос', color=VkKeyboardColor.PRIMARY)

        keyboard = keyboard.get_keyboard()
        return keyboard

def create_keyboard2():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Здравствуйте', color=VkKeyboardColor.PRIMARY)
    keyboard = keyboard.get_keyboard()
    return keyboard

now = datetime.now()  # получаем текущую дату и время
min_time = time(00, 00)  # от какого времени будет что-то работать
zan11 = time(9, 00)
zan12 = time(9, 45)
zan21 = time(9, 55)
zan22 = time(10, 40)
zan31 = time(11, 00)
zan32 = time(11, 45)
zan41 = time(12, 5)
zan42 = time(12, 50)
zan51 = time(13, 00)
zan52 = time(13, 45)
zan61 = time(13, 55)
zan62 = time(14, 40)
zan71 = time(14, 50)
zan72 = time(15, 35)
max_time = time(17, 00)  # до какого времени будет что-то работать

a = 1
users = {}
vopros = 'Вопрос в Сообщениях:'


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                #print(event.obj)
                user_id = event.obj.from_id
                if users.get(user_id)==None:
                    users[user_id] = a

                full_name = session_api.users.get(user_ids = event.obj.peer_id)
                priv = 'Здравствуйте, ' + full_name[0]['first_name']
                response = event.obj.text.lower()


                if response== 'здравствуйте':
                    keyboard = create_keyboard(response)
                    users[user_id] = 2

                if users[user_id] == 2:
                    keyboard = create_keyboard(response)
                    if not event.obj.from_group:
                        send_message(vk_session, event.obj.peer_id, message='Что Вы хотите узнать?', keyboard=keyboard)
                        users[user_id] = 3
                elif users[user_id] == 3 or users[user_id] == 10:
                    if not event.obj.from_group:
                        print(users[user_id])
                        if response == 'расписание':
                            attachment = f'photo-194565853_457239018'
                            send_message(vk_session,event.obj.peer_id, attachment= attachment)
                        elif response == 'какой сейчас урок?':
                             if now.time()>min_time and now.time()<zan11:
                                 send_message(vk_session, event.obj.peer_id, message='Занятия еще не начались')
                             elif now.time()>max_time:
                                 send_message(vk_session, event.obj.peer_id, message='Занятий нет')
                             elif now.time()>zan11 and now.time()<zan12:
                                 send_message(vk_session, event.obj.peer_id, message='Идет 1 урок')
                             elif now.time()>zan21 and now.time()<zan22:
                                  send_message(vk_session, event.obj.peer_id, message='Идет 2 урок')
                             elif now.time()>zan31 and now.time()<zan32:
                                    send_message(vk_session, event.obj.peer_id, message='Идет 3 урок')
                             elif now.time()>zan41 and now.time()<zan42:
                                    send_message(vk_session, event.obj.peer_id, message='Идет 4 урок')
                             elif now.time()>zan51 and now.time()<zan52:
                                     send_message(vk_session, event.obj.peer_id, message='Идет 5 урок')
                             elif now.time()>zan61 and now.time()<zan62:
                                      send_message(vk_session, event.obj.peer_id, message='Идет 6 урок')
                             elif now.time()>zan71 and now.time()<zan72:
                                       send_message(vk_session, event.obj.peer_id, message='Идет 7 урок')
                             elif (now.time()>zan12 and now.time()<zan21) or \
                                           (now.time()>zan22 and now.time()<zan31) or \
                                           (now.time()>zan32 and now.time()<zan41) or \
                                           (now.time()>zan42 and now.time()<zan51) or \
                                           (now.time()>zan52 and now.time()<zan61) or \
                                           (now.time()>zan62 and now.time()<zan71):
                                            send_message(vk_session, event.obj.peer_id, message='Сейчас перемена')
                        elif response == 'хочу задать вопрос':
                            send_message(vk_session, event.obj.peer_id, message='Напишите свой вопрос', keyboard=None)
                            print(user_id,users[user_id])
                            users[user_id] = 10

                        elif users[user_id] == 10:
                             vopros += '\n ' + response
                             keyboard = create_keyboard('u')
                             send_message(vk_session, event.obj.peer_id, message='Спасибо за вопрос.\n Мы ответим в ближайшее время.')
                             users[user_id] = 3
                             send_message(vk_session, 183736062 , message=vopros, keyboard=keyboard)

                             vopros = 'Вопрос в сообщениях:'
                else:
                    if not event.obj.from_group:
                        keyboard = create_keyboard2()

                        send_message(vk_session, event.obj.peer_id, message=priv, keyboard=keyboard)

        #версия с одним циклом
    except: pass
