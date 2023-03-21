from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging
from config import TOKEN, LOGIN, PASSWORD
import replymarkup as kb
import requests
from bs4 import BeautifulSoup as BS
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from random import randint
import os
import qrcode
import sympy as sp
import math as m

PROXY_URL = "https://proxy.server:3128"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'}
bot = Bot(token=TOKEN, proxy = PROXY_URL)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

# FSM Hello bot

@dp.message_handler(commands = ['start'], state = None)
async def hello_bot(message: types.Message):
    await bot.send_message(chat_id='690754165',
                           text=f'{message.chat.first_name} (@{message.chat.username}) воспользовался ботом')
    await bot.send_message(message.from_user.id, 'Привет, дружище. Меня зовут Вахумёнок, предлагаю тебе воспользоваться некоторыми функциями, нажми на одну кнопку из предложенных')

# FSM Hello bot

# Main Menu

@dp.message_handler(lambda message: 'Главное меню ⬅' in message.text)
@dp.message_handler(commands = ['menu'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отлично! Тогда предлагаю тебе воспользоваться некоторыми функциями, нажми на одну кнопку из предложенных', reply_markup = kb.startMenu)

@dp.message_handler(lambda message: 'Информация ℹ' in message.text)
async def information_about_bot(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ссылка на его ТГ ниже', reply_markup=kb.urlkb)
    await back_to_main_menu(message)

@dp.message_handler(lambda message: 'Игра 🎮' in message.text)
async def game_bot(message: types.Message):
    await bot.send_message(message.from_user.id, 'К сожалению, данная функция пока что в разработке. Надеюсь, мой разработчик когда-нибудь ее доделает. Будем пушка, отвечаю!')
    await back_to_main_menu(message)

# Main Menu

# QR CODE

class QRCODE(StatesGroup):
    user_url = State()
    create_qrcode = State()

def default_qrcode(url = 'google.com', name = 'default'):
    qr = qrcode.make(data = url)
    qr.save(stream = f'qrcode/{name}.jpeg')

@dp.message_handler(lambda message: 'Создать QRCODE' in message.text, state = None)
async def qrcode_url(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введи URL-ссылку: ')
    await QRCODE.create_qrcode.set()


@dp.message_handler(state = QRCODE.create_qrcode)
async def create_qr(message: types.Message, state: FSMContext):
    url = message.text
    await state.update_data(name = message.text)
    name = randint(1, 10)
    default_qrcode(url, str(name))
    photo = open(f'qrcode/{name}.jpeg', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    await bot.send_message(message.from_user.id, 'QRCODE успешно создан.\nХочешь выйти в Главное меню?', reply_markup = kb.backmainmenu)
    os.remove(f'qrcode/{name}.jpeg')
    await state.finish()


@dp.message_handler(lambda message: 'Курс Валюты 📈' in message.text)
async def main_get_value_currency(message: types.Message):
    async def get_usd_value():
        r = requests.get(
                'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0',
                headers=headers)
        html = BS(r.content, 'html.parser')
        usd = html.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': '2'})
        await get_euro_value(usd)

    async def get_euro_value(usd):
        r = requests.get('https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=AJOqlzUII_MMyTvBYZv8OCC1W_lYgjtgHA%3A1675645316502&ei=hFHgY4WyHvLwrwSE2Z6gCg&ved=0ahUKEwiFhPCe2f_8AhVy-IsKHYSsB6QQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIPCAAQsQMQgwEQQxBGEIICMgoIABCABBCxAxAKMgcIABCABBAKMgoIABCABBCxAxAKMgcIABCABBAKMgoIABCABBCxAxAKMgoIABCABBCxAxAKMgcIABCABBAKMg0IABCABBCxAxCDARAKMgcIABCABBAKOgoIABBHENYEELADOgcIABCwAxBDOgoIABCABBAUEIcCOgUIABCABDoJCAAQgAQQChAqOgQIIxAnOgoIABCxAxCDARBDOhAIABCABBAUEIcCELEDEIMBOgsIABCABBCxAxCDAToHCAAQsQMQQzoICAAQgAQQsQNKBAhBGABKBAhGGABQ5QdY_xZg5hhoBHABeACAAYUBiAGaBpIBAzcuMpgBAKABAcgBCsABAQ&sclient=gws-wiz-serp', headers = headers)
        html = BS(r.content, 'html.parser')
        euro = html.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': '2'})
        await get_bitcoin_value(usd, euro)

    async def get_bitcoin_value(usd, euro):
        r = requests.get('https://myfin.by/crypto-rates/bitcoin', headers=headers)
        html = BS(r.content, 'html.parser')
        bitcoin = html.findAll('div', {'class': 'birzha_info_head_rates'})
        await send_value_to_user(usd, euro, bitcoin)

    async def send_value_to_user(usd, euro, bitcoin):
        await bot.send_message(message.from_user.id, f'''Актуальный курс валюты на сегодня:
USD: {usd[0].text}₽
EUR: {euro[0].text}₽
BTC: {str(bitcoin[0].text.strip())}''')
        await back_to_main_menu(message)
    await get_usd_value()

# ПРОИЗВОДНАЯ ФУНКЦИИ

class DerivativeFSM(StatesGroup):
    send_derivative_function_users = State()

@dp.message_handler(lambda message: 'Найти производную функции' in message.text)
async def derivative(message: types.Message):
    await bot.send_message(message.from_user.id, 'Напиши исходную функцию (x^2 + 5 * x + 6)')
    await DerivativeFSM.next()

@dp.message_handler(state = DerivativeFSM.send_derivative_function_users)
async def send_derivative(message: types.Message, state: FSMContext):
    function_user = message.text
    print(function_user)
    try:
        x = sp.symbols('x')
        function_user_diff = sp.diff(function_user, x)
        function_user_simplify = sp.simplify(function_user_diff)
        await bot.send_message(message.from_user.id, function_user_simplify)
        await state.finish()
        await back_to_main_menu(message)
    except:
        await state.finish()
        await bot.send_message(message.from_user.id, 'Что-то пошло не так')
        await derivative(message)

# ПРОИЗВОДНАЯ ФУКНЦИИ

# НЕ РАСПОЗНАЛ | ВОЗВРАЩЕНИЕ В ГЛАВНОЕ МЕНЮ

async def back_to_main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Хочешь вернуться в Главное Меню?', reply_markup = kb.backmainmenu)

@dp.message_handler()
async def handler_except(message: types.Message):
    await bot.send_message(message.from_user.id, text = 'Я не смог распознать твое сообщение, вернуться в Главное меню?', reply_markup=kb.backmainmenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
