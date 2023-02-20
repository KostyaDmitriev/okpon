from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

schedule = {
    'Расписание': {
        'Карате (для детей 4-6 лет)': {
            'Вторник': [16.30],
            'Четверг': [16.30],
        },
        'Карате (для детей  7-18 лет)': {
            'Понедельник': [17.30],
            'Вторник': [17.30, 19.00],
            'Среда': [17.30],
            'Четверг': [17.30, 19.00],
            'Пятница': [17.30],
            "Суббота": [11.00]
        },
        'Карате для взрослых': {
            'Понедельник': [21.00],
            'Среда': [21.00],
            'Пятница': [21.00],
        }
    }
}

API_TOKEN = '5849805697:AAHBqNJgSjwIu0jxDcgquEawIQVThstOefc'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
start_message = '''Привет это телеграмм бот Dojo S.K.1
В этом боте ты можешь записаться на тренировки по карате\n
Для навигации используй следующие команды:\nПосмотреть расписание по дням: /days
Посмотреть расписание по секциям: /section
Показать стартовое сообщение: /start\nПомощь по командам бота: /help'''


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(start_message)


buttons_days = [InlineKeyboardButton('Понедельник', callback_data='butd1'),
                InlineKeyboardButton('Вторник', callback_data='butd2'),
                InlineKeyboardButton('Среда', callback_data='butd3'),
                InlineKeyboardButton('Четверг', callback_data='butd4'),
                InlineKeyboardButton('Пятница', callback_data='butd5'),
                InlineKeyboardButton('Суббота', callback_data='butd6')]
keyboard = InlineKeyboardMarkup(row_width=2).add(*buttons_days)

butd135 = [17.30]
keyboard_butd135 = InlineKeyboardMarkup(row_width=2).add(*butd135)

butd24 = [17.30, 19.00]
keyboard_butd24 = InlineKeyboardMarkup(row_width=2).add(*butd24)

butd6 = [11.00, 12.00]
keyboard_butd6 = InlineKeyboardMarkup(row_width=2).add(*butd6)

@dp.callback_query_handler(func=lambda c: c.data == ['butd1', 'butd3', 'butd5'])
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите время:', reply_markup=keyboard_butd135)

@dp.callback_query_handler(func=lambda c: c.data == ['butd2', 'butd4'])
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите время:', reply_markup=keyboard_butd24)

@dp.callback_query_handler(func=lambda c: c.data == 'butd6')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите время:', reply_markup=keyboard_butd6)

@dp.message_handler(commands=['days'])
async def send_days(message):
    await message.reply('Выберите день:', reply_markup=keyboard)


buttons_section = [InlineKeyboardButton('Карате (4-6 лет)', callback_data='buts1'),
                   InlineKeyboardButton('Карате (6-18 лет)', callback_data='buts2'),
                   InlineKeyboardButton('Карате для взрослых (18+)', callback_data='buts3')]
keyboard2 = InlineKeyboardMarkup.add(*buttons_section)
buts1 = [InlineKeyboardButton('Вторник', callback_data='butd12'), InlineKeyboardButton('Четверг', callback_data='butd14')]
keyboard_buts1 = InlineKeyboardMarkup(row_width=2).add(*buts1)

buts1_time = [16.30]
keyboard_buts1_time = InlineKeyboardMarkup(row_width=2).add(*buts1_time)

@dp.callback_query_handler(func=lambda c: c.data == 'buts1')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите день:', reply_markup=keyboard_buts1)

@dp.callback_query_handler(func=lambda c: c.data == ['buts12', 'buts14'])
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите день:', reply_markup=keyboard_buts1_time)

@dp.message_handler(commands=['section'])
async def send_section(message):
    await message.reply('Выберите секцию:', reply_markup=keyboard2)


@dp.message_handler()
async def send_idk(message: types.Message):
    await message.reply('Я ещё не умею отвечать на эту команду')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
