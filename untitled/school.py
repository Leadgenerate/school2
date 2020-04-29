import sys
from time import timezone


from datetime import datetime, date, time
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime, timedelta
from datetime import time
import random

token = "5a9d9af0a94f9c7e9551de8bb9322799ca4be14e13267b30c0000ebf046d0f23946c89c4cd8855fb96ec3"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)



def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})



def create_keyboard(response):
     keyboard = VkKeyboard(one_time=False)
     response = event.text.lower()
     if event.from_user and not (event.from_me):

           if response == 'здравствуйте':
                keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)

                keyboard.add_line()  # Переход на вторую строку
                keyboard.add_button('Какой сейчас урок?', color=VkKeyboardColor.POSITIVE)

                keyboard.add_line()
                keyboard.add_button('Хочу задать вопрос', color=VkKeyboardColor.PRIMARY)

                keyboard = keyboard.get_keyboard()
                return keyboard

def create_keyboard2(response):
     keyboard = VkKeyboard(one_time=False)
     response = event.text.lower()
     if event.from_user and not (event.from_me):
        if event.type == VkEventType.MESSAGE_NEW:
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

vopros = 'Вопрос в Сообщениях:'

for event in longpoll.listen():
   if event.type == VkEventType.MESSAGE_NEW and not (a>1):
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print('Ссылка на пользователя: vk.com/id'+str(event.user_id))
        full_name = session_api.users.get(user_ids = event.peer_id)
        priv = 'Здравствуйте, ' + full_name[0]['first_name']
        response = event.text.lower()
        keyboard = create_keyboard2(response)

        if event.from_user and not (event.from_me):
          send_message(vk_session, 'user_id', event.user_id, message=priv, keyboard=keyboard)
          a+= 1
          break


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and (a == 2):
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print('Ссылка на пользователя: vk.com/id'+str(event.user_id))
        response = event.text.lower()
        keyboard = create_keyboard(response)
        if event.from_user and not (event.from_me):
          send_message(vk_session, 'user_id', event.user_id, message='Что Вы хотите узнать?', keyboard=keyboard)
          a+= 1
          break


for event in longpoll.listen():
 if event.type == VkEventType.MESSAGE_NEW and (a == 3):
    print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
    print('Текст сообщения: ' + str(event.text))
    print('Ссылка на пользователя: vk.com/id'+str(event.user_id))
    response = event.text.lower()
    if event.from_user and not (event.from_me):
      response = event.text.lower()
      if response == 'расписание':
          attachment = f'photo-194565853_457239018'
          send_message(vk_session, 'user_id', event.user_id, attachment= attachment)


      elif response == 'какой сейчас урок?':
             if now.time()>min_time and now.time()<zan11:
               send_message(vk_session, 'user_id', event.user_id, message='Занятия еще не начались')
             elif now.time()>max_time:
                 send_message(vk_session, 'user_id', event.user_id, message='Занятий нет')
             elif now.time()>zan11 and now.time()<zan12:
                 send_message(vk_session, 'user_id', event.user_id, message='Идет 1 урок')
             elif now.time()>zan21 and now.time()<zan22:
                  send_message(vk_session, 'user_id', event.user_id, message='Идет 2 урок')
             elif now.time()>zan31 and now.time()<zan32:
                   send_message(vk_session, 'user_id', event.user_id, message='Идет 3 урок')
             elif now.time()>zan41 and now.time()<zan42:
                    send_message(vk_session, 'user_id', event.user_id, message='Идет 4 урок')
             elif now.time()>zan51 and now.time()<zan52:
                     send_message(vk_session, 'user_id', event.user_id, message='Идет 5 урок')
             elif now.time()>zan61 and now.time()<zan62:
                      send_message(vk_session, 'user_id', event.user_id, message='Идет 6 урок')
             elif now.time()>zan71 and now.time()<zan72:
                       send_message(vk_session, 'user_id', event.user_id, message='Идет 7 урок')
             elif (now.time()>zan12 and now.time()<zan21) or \
                           (now.time()>zan22 and now.time()<zan31) or \
                           (now.time()>zan32 and now.time()<zan41) or \
                           (now.time()>zan42 and now.time()<zan51) or \
                           (now.time()>zan52 and now.time()<zan61) or \
                           (now.time()>zan62 and now.time()<zan71):
                              send_message(vk_session, 'user_id', event.user_id, message='Сейчас перемена')
                              a=3

      elif response == 'хочу задать вопрос':
        send_message(vk_session, 'user_id', event.user_id, message='Напишите свой вопрос')
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print('Ссылка на пользователя: vk.com/id'+str(event.user_id))
        for event in longpoll.listen():
         if event.type == VkEventType.MESSAGE_NEW:
          print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
          print('Текст сообщения: ' + str(event.text))
          print('Ссылка на пользователя: vk.com/id'+str(event.user_id))
          response = event.text.lower()
          if event.from_user and not (event.from_me):
             vopros += '\n ' + response
             send_message(vk_session, 'user_id', event.user_id, message='Спасибо за вопрос.\n Мы ответим в ближайшее время.')
             send_message(vk_session, 'user_id',183736062 , message=vopros)
             vopros = 'Вопрос в сообщениях:'
             a=3
             break
