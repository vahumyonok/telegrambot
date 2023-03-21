from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# Main menu

#******************************* REPLY MARKUP ************************************#

btnCurrency = KeyboardButton('Курс Валюты 📈')
btnInformation = KeyboardButton('Информация ℹ')
btnCalculator = KeyboardButton('Игра 🎮')
btnQRCODE = KeyboardButton('Создать QRCODE ✏️')
btnDerivative = KeyboardButton('Найти производную функции')
startMenu = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= True).add(btnCurrency, btnInformation).row(btnCalculator, btnQRCODE, btnDerivative)

btnMainMenu = KeyboardButton('Главное меню ⬅')
backmainmenu = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard= True).add(btnMainMenu)


btnCurrencyCalculator = KeyboardButton('Конвертер Валют 📱')
btnBackMainMenu = KeyboardButton('Главное меню ⬅')
CurrencyCalculator = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(btnCurrencyCalculator, btnBackMainMenu)

btnUSDsell = KeyboardButton('Продать Доллар Банку')
btnUSDbuy = KeyboardButton('Купить Доллар у Банка')
sellbuyUSD = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(btnUSDbuy, btnUSDsell)

btnEURsell = KeyboardButton('Продать Евро Банку')
btnEURbuy = KeyboardButton('Купить Евро у Банка')
sellbuyEUR = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(btnEURbuy, btnEURsell)

btnYES = KeyboardButton('Да')
btnNO = KeyboardButton('Нет')
keyboardyesno = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(btnYES, btnNO)

#************************************* INLINE MARKUP *******************************#

btnURLTelegram = InlineKeyboardButton('Telegram', url = 't.me/vahumyonok', callback_data= 'Telegram')
urlkb = InlineKeyboardMarkup(row_width=1).add(btnURLTelegram)

btnKnow = InlineKeyboardButton('Статья', url = 'https://bankstoday.net/vopros-otvet/pochemu-kupit-valyutu-dorozhe-chem-prodat', callback_data = 'Know')
alertkb = InlineKeyboardMarkup(row_width = 1).add(btnKnow)

btnUSD = KeyboardButton('USD')
btnEUR = KeyboardButton('EUR')
btnBTC = KeyboardButton('BTC')
btnMainMenuCalculator = KeyboardButton('Главное меню ⬅')
keyboard_currency = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard = True).add(btnUSD, btnEUR, btnBTC).row(btnMainMenuCalculator)

btnDelete = InlineKeyboardButton('Удалить', callback_data = 'delete')
keyboard_delete = InlineKeyboardMarkup(row_width = 1).add(btnDelete)

btnText = InlineKeyboardButton('Текста', callback_data = 'text')
keyboard_admin = InlineKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(btnText)