from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from aiogram.types.message.Message import sendMessage


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

API_TOKEN = '5849805697:AAENDBPqfJZ5TSVuksQgWYi8lo-BoEB4sX8'

# Initialize bot and dispatcher
PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)
start_message = '''Привет это телеграмм бот Dojo S.K.1
В этом боте ты можешь записаться на тренировки по карате
Для навигации используй следующие команды:
Посмотреть расписание по секциям: /section
Показать стартовое сообщение: /start
Помощь по командам бота: /help'''


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

butd135 = [InlineKeyboardButton('17.30', callback_data='butd1351')]
keyboard_butd135 = InlineKeyboardMarkup(row_width=1).add(*butd135)

butd24 = [InlineKeyboardButton('17.30', callback_data='butd241'), InlineKeyboardButton('19.00', callback_data='butd242')]
keyboard_butd24 = InlineKeyboardMarkup(row_width=2).add(*butd24)

butd6 = [InlineKeyboardButton('11.00', callback_data='butd61'), InlineKeyboardButton('12.00', callback_data='butd62')]
keyboard_butd6 = InlineKeyboardMarkup(row_width=2).add(*butd6)

@dp.callback_query_handler(lambda c: c.data == 'butd2')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вторник\nВыберите время:', reply_markup=keyboard_butd24)

@dp.callback_query_handler(lambda c: c.data == 'butd4')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали четверг\nВыберите время:', reply_markup=keyboard_butd24)

@dp.callback_query_handler(lambda c: c.data == 'butd1')
async def process_callback_section(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали понедельник\nВыберите время:', reply_markup=keyboard_butd135)

@dp.callback_query_handler(lambda c: c.data == 'butd3')
async def process_callback_section(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали среду\nВыберите время:', reply_markup=keyboard_butd135)

@dp.callback_query_handler(lambda c: c.data == 'butd5')
async def process_callback_section(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали пятницу\nВыберите время:', reply_markup=keyboard_butd135)

@dp.callback_query_handler(lambda c: c.data == 'butd6')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали субботу\nВыберите время:', reply_markup=keyboard_butd6)

@dp.message_handler(commands=['days'])
async def send_days(message):
    await message.reply('Выберите день:', reply_markup=keyboard)


buttons_section = [InlineKeyboardButton('Карате (4-6 лет)', callback_data='buts1'),
                   InlineKeyboardButton('Карате (6-18 лет)', callback_data='buts2'),
                   InlineKeyboardButton('Карате для взрослых (18+)', callback_data='buts3')]
keyboard2 = InlineKeyboardMarkup(row_width=2).add(*buttons_section)
buts1 = [InlineKeyboardButton('Вторник', callback_data='buts12'), InlineKeyboardButton('Четверг', callback_data='buts14')]
keyboard_buts1 = InlineKeyboardMarkup(row_width=2).add(*buts1)

buts1_time = [InlineKeyboardButton('16.30', callback_data='buts1time1')]
keyboard_buts1_time = InlineKeyboardMarkup(row_width=1).add(*buts1_time)

buttons_dayss = [InlineKeyboardButton('Понедельник', callback_data='butd1s'),
                InlineKeyboardButton('Вторник', callback_data='butd2s'),
                InlineKeyboardButton('Среда', callback_data='butd3s'),
                InlineKeyboardButton('Четверг', callback_data='butd4s'),
                InlineKeyboardButton('Пятница', callback_data='butd5s'),
                InlineKeyboardButton('Суббота', callback_data='butd6s')]
keyboards = InlineKeyboardMarkup(row_width=2).add(*buttons_dayss)

butd135s = [InlineKeyboardButton('17.30', callback_data='butd1351s')]
keyboard_butd135s = InlineKeyboardMarkup(row_width=1).add(*butd135s)

butd24s = [InlineKeyboardButton('17.30', callback_data='butd241s'), InlineKeyboardButton('19.00', callback_data='butd242s')]
keyboard_butd24s = InlineKeyboardMarkup(row_width=2).add(*butd24s)

butd6s = [InlineKeyboardButton('11.00', callback_data='butd61s'), InlineKeyboardButton('12.00', callback_data='butd62s')]
keyboard_butd6s = InlineKeyboardMarkup(row_width=2).add(*butd6s)


buts3 = [InlineKeyboardButton('Понедельник', callback_data='buts31'),
         InlineKeyboardButton('Среда', callback_data='buts33'),
         InlineKeyboardButton('Пятница', callback_data='buts35')]
buts3kb = InlineKeyboardMarkup(row_width=3).add(*buts3)

buts3_time = [InlineKeyboardButton('21.00', callback_data='buts3time')]
buts3_timekb = InlineKeyboardMarkup(row_width=1).add(*buts3_time)


@dp.callback_query_handler(lambda c: c.data == 'buts35')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали пятницу\nВыберите время:', reply_markup=buts3_timekb)

@dp.callback_query_handler(lambda c: c.data == 'buts33')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали среду\nВыберите время:', reply_markup=buts3_timekb)

@dp.callback_query_handler(lambda c: c.data == 'buts31')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали понедельник\nВыберите время:', reply_markup=buts3_timekb)

@dp.callback_query_handler(lambda c: c.data == 'buts3')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали карате для взрослых(18+)\nВыберите день:', reply_markup=buts3kb)


@dp.callback_query_handler(lambda c: c.data == 'butd2s')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вторник\nВыберите время:', reply_markup=keyboard_butd24s)

@dp.callback_query_handler(lambda c: c.data == 'butd4s')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали четверг\nВыберите время:', reply_markup=keyboard_butd24s)

@dp.callback_query_handler(lambda c: c.data == 'butd1s')
async def process_callback_section(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали понедельник\nВыберите время:', reply_markup=keyboard_butd135s)

@dp.callback_query_handler(lambda c: c.data == 'butd3s')
async def process_callback_section(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали среду\nВыберите время:', reply_markup=keyboard_butd135s)

@dp.callback_query_handler(lambda c: c.data == 'butd5s')
async def process_callback_section(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали пятницу\nВыберите время:', reply_markup=keyboard_butd135s)

@dp.callback_query_handler(lambda c: c.data == 'butd6s')
async def process_callback_section(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали субботу\nВыберите время:', reply_markup=keyboard_butd6s)

@dp.callback_query_handler(lambda c: c.data == 'buts2')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали карате для детей(6-18 лет)\nВыберите день:', reply_markup=keyboards)

@dp.callback_query_handler(lambda c: c.data == 'buts12')
async def process_callbcion(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вторник\nВыберите время:', reply_markup=keyboard_buts1_time)

@dp.callback_query_handler(lambda c: c.data == 'buts14')
async def process_callbction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали четверг\nВыберите время:', reply_markup=keyboard_buts1_time)

@dp.callback_query_handler(lambda c: c.data == 'buts1')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали карате для детей(4-6 лет)\nВыберите день:', reply_markup=keyboard_buts1)

@dp.message_handler(commands=['section'])
async def send_section(message):
    await message.reply('Выберите секцию:', reply_markup=keyboard2)



@dp.callback_query_handler(lambda c: c.data == 'butd241s')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'butd242s')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'butd1351s')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'butd61s')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'butd62s')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'buts12')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'buts14')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'buts3time')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.callback_query_handler(lambda c: c.data == 'buts1time1')
async def process_calction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Что записаться на тренировки по карате пожалуйста обратитесь по данному номеру: +7 916 400 4288 или @dojo_sk1')

@dp.message_handler()
async def send_idk(message: types.Message):
    await message.reply('Я ещё не умею отвечать на эту команду')

async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
