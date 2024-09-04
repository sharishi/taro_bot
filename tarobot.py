import random

import telebot
from telebot import types
from infobase import card_desc, way, colors_array, events_array, horoscopes
from settings import token

bot = telebot.TeleBot(token)


def create_zodiac_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    zodiac_signs = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
    buttons = [types.InlineKeyboardButton(text=sign, callback_data=sign) for sign in zodiac_signs]
    keyboard.add(*buttons)
    return keyboard


def draw_tarot_card():
    card_number = random.randint(0, 21)  # Здесь 21 - количество карт в вашей колоде Таро
    return card_number, card_desc[card_number]


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🔮 Аркан дня')
    item2 = types.KeyboardButton('🎱 Число дня')
    item3 = types.KeyboardButton('🧿 Цвет дня')
    item4 = types.KeyboardButton('🪄 Событие дня')
    item5 = types.KeyboardButton('🪬 Гороскоп дня')
    item6 = types.KeyboardButton('Другое...')

    # 🎱🔮📿🧿🪄🪬
    markup.add(item1, item2, item3, item4, item5, item6)
    text = 'Приветствую тебя, {0.first_name}! '
    bot.send_message(message.chat.id, text.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    """Команды для чата в личных сообщениях"""
    if message.chat.type == 'private':
        """Просмотр числа дня"""
        if message.text == '🎱 Число дня':
            temp_daynum = random.randint(1, 77)
            bot.send_message(message.chat.id, '✨Ваше число дня✨: ' + str(temp_daynum))
            """Просмотр аркана дня"""
        elif message.text == '🔮 Аркан дня':
            temp_daycard = random.randint(0, 21)
            bot.send_message(message.chat.id, '✨Ваш аркан дня✨: ' + str(temp_daycard))
            bot.send_message(message.chat.id, '✨Описание вашего аркана дня✨: \n')
            img = open(way + str(temp_daycard) + '.png', 'rb')
            bot.send_photo(message.chat.id, img, caption=card_desc[temp_daycard])
            """Просмотр цвета дня"""
        elif message.text == '🧿 Цвет дня':
            bot.send_message(message.chat.id, '✨Ваш цвет дня✨: ' + str(random.choice(colors_array)))
            """Дополнительная кнопка, чтобы добавить новые функции"""
        elif message.text == '🪄 Событие дня':
            bot.send_message(message.chat.id, '✨Событие дня✨:\n' + random.choice(events_array))
        elif message.text == '🪬 Гороскоп дня':
            keyboard = create_zodiac_keyboard()
            bot.send_message(message.chat.id, 'Выберите ваш знак зодиака:', reply_markup=keyboard)
        elif message.text == 'Получу ли я 10 за индивидуальную по php?':
            bot.send_message(message.chat.id, "Разумеется да! У Вас просто прекрасная работа! "
                                              "P.S. Мне очень нравится здесь работать!")
        elif message.text.endswith('?') or 'предсказание' in message.text.lower():
            card_number, card_description = draw_tarot_card()
            bot.send_message(message.chat.id, f'Вы тянете карту Таро... 🃏\n\n{card_description}')
            bot.send_message(message.chat.id, f'Мой финальный ответ: {random.choice(["ДА", "НЕТ"])}')
        elif message.text == 'Другое...':
            bot.send_message(message.chat.id,
                             'Я начинающий маг, поэтому другие возможности покажу позже...\nНажмите /start и попробуйте снова✨')
        else:
            """Если пользователь ввел неверные символы, то ему бот выдаст ошибку"""
            bot.send_message(message.chat.id,
                             'Проводя различные манипуляции с магией, я перестал Вас понимать,\nнажмите /start и попробуйте снова✨')

            """Команды бота для групповых чатов"""
            """Описание функций одинаковое, но убрано реагирование бота на обычные сообщения"""
    if message.chat.type != 'private':
        if message.text == '🎱 Число дня':
            temp_daynum = random.randint(1, 77)
            bot.send_message(message.chat.id, '✨Ваше число дня✨: ' + str(temp_daynum))
        elif message.text == '🔮 Аркан дня':
            temp_daycard = random.randint(0, 21)
            bot.send_message(message.chat.id, '✨Ваш аркан дня✨: ' + str(temp_daycard))
            bot.send_message(message.chat.id, '✨Описание вашего аркана дня✨: \n')
            img = open(way + str(temp_daycard) + '.jpeg', 'rb')
            bot.send_photo(message.chat.id, img, caption=card_desc[temp_daycard])
        elif message.text == '🧿 Цвет дня':
            bot.send_message(message.chat.id, '✨Ваш цвет дня✨: ' + str(random.choice(colors_array)))
        elif message.text == '🪄 Событие дня':
            bot.send_message(message.chat.id, '✨Событие дня✨:\n' + random.choice(events_array))
        elif message.text == '🪬 Гороскоп дня':
            keyboard = create_zodiac_keyboard()
            bot.send_message(message.chat.id, 'Выберите ваш знак зодиака:', reply_markup=keyboard)
        elif message.text.endswith('?') or 'предсказание' in message.text.lower():
            card_number, card_description = draw_tarot_card()
            bot.send_message(message.chat.id, f'Вы тянете карту Таро... 🃏\n\n{card_description}')
        elif message.text == 'Другое...':
            bot.send_message(message.chat.id,
                             'Я начинающий маг, поэтому другие возможности покажу позже...\nНажмите /start и попробуйте снова✨')

@bot.callback_query_handler(func=lambda call: True)
def handle_zodiac_sign(call):
    user_sign = call.data
    if user_sign in horoscopes:
        prediction = random.choice(horoscopes[user_sign])
        bot.send_message(call.message.chat.id, f'✨ Гороскоп для {user_sign}: {prediction}')
    else:
        bot.send_message(call.message.chat.id, 'К сожалению, для вашего знака зодиака нет предсказаний.')


bot.polling(none_stop=True)
