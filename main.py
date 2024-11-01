import telebot
from random import randint
from time import sleep

cards_data = [
    {
        'pathToImg': 'asleep',
        'category': 'Стандартный пак Lovely Peaches',
        'era': 'Обычная',
        'caption': 'Спящий гном'
    },
    {
        'pathToImg': 'barbie',
        'category': 'Магический пак Lovely Peaches',
        'era': 'Редкая',
        'caption': 'А я Peaches-girl, играю я в котёл'
    },
    {
        'pathToImg': 'bcardi',
        'category': 'Тефтелевый пак',
        'era': 'Легендарная',
        'caption': 'Блинница'
    },
    {
        'pathToImg': 'colorful',
        'category': 'Магический пак Lovely Peaches',
        'era': 'Редкая',
        'caption': 'Сплит'
    },
    {
        'pathToImg': 'crying',
        'category': 'Стандартный пак Lovely Peaches',
        'era': 'Обычная',
        'caption': 'What was I made for...'
    },
    {
        'pathToImg': 'fashion',
        'category': 'Стандартный пак Lovely Peaches',
        'era': 'Обычная',
        'caption': 'Модный приговор'
    },
    {
        'pathToImg': 'french',
        'category': 'Магический пак Lovely Peaches',
        'era': 'Редкая',
        'caption': "J'ai besoin de plus d'Ozempic"
    },
    {
        'pathToImg': 'hehe',
        'category': 'Стандартный пак Lovely Peaches',
        'era': 'Обычная',
        'caption': 'Ненавидь меня — это чизбургериально'
    },
    {
        'pathToImg': 'jimin',
        'category': 'Тефтелевый пак',
        'era': 'Легендарная',
        'caption': 'Džimin'
    },
    {
        'pathToImg': 'laught',
        'category': 'Стандартный пак Lovely Peaches',
        'era': 'Обычная',
        'caption': 'Когда топик влез в ручную кладь'
    },
    {
        'pathToImg': 'mdna',
        'category': 'Тефтелевый пак',
        'era': 'Легендарная',
        'caption': 'Доча, дай сфоткаю тебя в вагоне'
    },
    {
        'pathToImg': 'smile',
        'category': 'Стандартный пак Lovely Peaches',
        'era': 'Обычная',
        'caption': 'Смоки ноздри'
    },
    {
        'pathToImg': 'tongue',
        'category': 'Стандартный пак Lovely Peaches',
        'era': 'Обычная',
        'caption': 'Мужиковатое'
    },
]

bot = telebot.TeleBot('7830246065:AAElndBwVD2cecTOdORcpbmW1kJTu4jHCxE')


@bot.message_handler(commands=['start'])
def start(message):
    print('here')
    bot.send_message(message.chat.id,
                     "Привет-привет!👋\nМеня зовут Алена Джексон 2.0. Я - прокаченная версия своей сестры Алены Джексон 1.0.\nЯ растворила эту падаль в субстанции👩‍🔬 и взяла от нее только самое лучшее😉\nСо мной ты точно не соскучишься🧚🏿\nМои команды:\n/about - узнать кто ты по рангу (временно не работает)\n/newpet - завести нового питомца (временно не работает)\n/mypets - показать моих питомцов (временно не работает)\n/gacha - крутить lovely peaches-гачу")

@bot.message_handler(commands=['peaches'])
def start(message):
    print('here')
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('ДА', url='https://www.youtube.com/watch?v=WCNBv7ybwTU')
    btn2 = telebot.types.InlineKeyboardButton('Хорс таун', url='https://www.youtube.com/watch?v=22wH0n-Y-jM')
    markup.add(btn1)  # создаем строку с 2 кнопками
    markup.add(btn2)
    bot.send_message(message.chat.id,
                     "Хотите увидеть Олега?!👋n", reply_markup=markup)


@bot.message_handler(commands=['gacha'])
def gacha(message):
    gif = open("lovely_peaches/gacha.gif", 'rb')
    message_with_gif = bot.send_animation(message.chat.id, gif, caption='Вам падает🌠')
    gif.close()

    sleep(1.5)

    card = cards_data[randint(0, len(cards_data) - 1)]
    text = f"⛓️Вам выпал(а): {card['caption']}\n🃏Пак: {card['category']}\n🦧Эра: {card['era']}"

    photo = open(f"lovely_peaches/{card['pathToImg']}.jpg", 'rb')

    bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        reply_to_message_id=message.message_id,
        caption=text
    )

    stickers = {
        'Стандартный пак Lovely Peaches': 'CAACAgIAAxkBAAEJgoNnHn2mZv74vSv64crMd29A2egMzQACk08AAjazqUkjplqIJ4cTnTYE',
        'Магический пак Lovely Peaches': 'CAACAgIAAxkBAAEJgodnHn4qdhtdjy3jMcmvC9sdhE1JtQACLlAAAgNtKUkSGlePaV32ZzYE',
        'Тефтелевый пак': 'CAACAgIAAxkBAAEJgolnHn5o1loE5liSipgCwE-PFLO6lgAClFEAAkOZIUob6dzludKWRzYE',
    }

    bot.send_sticker(message.chat.id, stickers[card['category']])
    photo.close()

    # bot.reply_to(message, 'Hey!')
    bot.delete_message(message.chat.id, message_with_gif.message_id)


@bot.message_handler(content_types=['text'])
def answer_text(message):
    words = message.text.lower().strip().split()
    if words == ['муд', 'или', 'вайб'] or message.text.lower().strip().split() == [
        'вайб', 'или', 'муд']:
        bot.reply_to(message, f"Как по мне - это {['вайб', 'муд'][randint(0, 1)]}💁‍♀️")
    elif words == ['облить', 'субстанцией']:
        if message.reply_to_message:
            replied_user = message.reply_to_message.from_user.username

            bot.send_message(message.chat.id, f'@{message.from_user.username} Обливает субстанцией @{replied_user}!👩‍🔬')
    elif words == ['отобрать', 'оземпик']:
        if message.reply_to_message:
            replied_user = message.reply_to_message.from_user.username

            bot.send_message(message.chat.id, f'@{message.from_user.username} Забирает последний Ozempic у @{replied_user}!👩‍')
    elif words == ['добавить', 'жир']:
        if message.reply_to_message:
            replied_user = message.reply_to_message.from_user.username

            body_parts = ['пятку', 'лоб', 'бровь', 'веко', 'голень', 'палец', 'пупок']
            bot.send_message(message.chat.id, f'@{message.from_user.username} Добавляет жир Пичес в {body_parts[randint(0, len(body_parts) - 1)]} @{replied_user}!👩‍🔬')
    elif words == ['варн']:
        if message.reply_to_message:
            replied_user = message.reply_to_message.from_user.username

            body_parts = ['пятку', 'лоб', 'бровь', 'веко', 'голень', 'палец', 'пупок']
            bot.send_message(message.chat.id,
                             f'Вы не можете варновать @{replied_user}! У нас коммунизм🤦‍♀️‍')
    elif words == ['я', 'и', 'кто']:
        # photo = open(f'lovely_peaches/{card['pathToImg']}.jpg', 'rb')
        # bot.send_message(message.chat.id,
        #                 'Я тупая как пробка от швепса')
        with open('lovely_peaches/kim.jpg', 'rb') as f:
            bot.send_photo(
            chat_id = message.chat.id,
            photo = f,
            caption = 'И он')


bot.polling(none_stop=True)
