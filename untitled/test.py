import sys

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time

token = "3cbadf7754a4e2beaa1bd0ef9b6a9eb94d216f1bcba27ecd922aef1d7015a3707297271e9a403ed517531"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

     if response == 'тест':

        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)