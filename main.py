'''
Асинхронный телегамм-бот на Python
Для реализации общей асинхронной рассылки необходимы ID пользователей-получателей
А дальше уже по-классике, бегаем циклом по БД или массиву и шлём сообщения направо и налево
Как вариант, можно сохранять ID пользователей при старте бота
ID пользователя можно получить из объекта сообщения - msg.from_user.id
Ссылка на бота - @aiogram_omk_bot, согласно введённому токену
'''
from aiogram import Bot, types, Dispatcher, executor


bot = Bot(token='7139950940:AAEXEaLlSjb48dEQfjSsL231Ip4_JI1IqUs')
dp = Dispatcher(bot)

user_id = []


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id.append(str(message.from_user.id))
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


async def send_everyone(message):
    for user in user_id:
        await bot.send_message(user, message)


if __name__ == '__main__':
    executor.start_polling(dp)
